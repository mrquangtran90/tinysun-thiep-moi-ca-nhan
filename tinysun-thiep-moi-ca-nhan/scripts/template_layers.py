"""Static, self-contained SVG layer replacement. No image generation or editing."""
import argparse
import base64
import copy
import hashlib
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

SVG = "http://www.w3.org/2000/svg"
XLINK = "http://www.w3.org/1999/xlink"
ET.register_namespace("", SVG)
ET.register_namespace("xlink", XLINK)
DATA = re.compile(r"data:image/(png|jpeg|webp);base64,([A-Za-z0-9+/=\s]+)\Z")


def local(tag):
    return tag.rsplit("}", 1)[-1]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def raster_type(data):
    if data.startswith(b"\x89PNG\r\n\x1a\n"):
        return "png"
    if data.startswith(b"\xff\xd8\xff"):
        return "jpeg"
    if data.startswith(b"RIFF") and data[8:12] == b"WEBP":
        return "webp"
    raise ValueError("Only actual PNG, JPEG or WebP image bytes are supported")


def decode_image(value):
    match = DATA.fullmatch(value)
    if not match:
        raise ValueError("Image must be embedded PNG/JPEG/WebP data, not a remote file")
    data = base64.b64decode(re.sub(r"\s", "", match[2]), validate=True)
    if raster_type(data) != match[1]:
        raise ValueError("Image MIME does not match signature")
    return data


def load_template(filename):
    data = Path(filename).read_bytes()
    if len(data) > 100 * 1024 * 1024:
        raise ValueError("Template exceeds 100 MiB")
    text = data.decode("utf-8-sig")
    if re.search(r"<!DOCTYPE|<!ENTITY|<\?xml-stylesheet|@import|@font-face", text, re.I):
        raise ValueError("Dynamic/external SVG resources are unsupported")
    root = ET.fromstring(text)
    if root.tag != f"{{{SVG}}}svg":
        raise ValueError("Expected namespaced SVG root")
    ids = set()
    for el in root.iter():
        if local(el.tag).lower() in {"script", "foreignobject", "animate", "animatetransform", "set"}:
            raise ValueError("Only static SVG templates are supported")
        ident = el.get("id")
        if ident:
            if ident in ids:
                raise ValueError(f"Duplicate ID: {ident}")
            ids.add(ident)
        for key, value in el.attrib.items():
            attr = local(key).lower()
            if attr.startswith("on") or attr == "base":
                raise ValueError("Event handlers and xml:base are unsupported")
            if attr == "href":
                if local(el.tag) == "image":
                    decode_image(value)
                elif not value.startswith("#"):
                    raise ValueError("External href is unsupported")
        css = " ".join(el.attrib.values())
        if local(el.tag) == "style":
            css += el.text or ""
        for ref in re.findall(r"url\s*\(([^)]*)\)", css, re.I):
            if not ref.strip(" \t\r\n\"'").startswith("#"):
                raise ValueError("External CSS URL is unsupported")
        if local(el.tag) == "style" and "\\" in (el.text or ""):
            raise ValueError("Escaped CSS is unsupported")
    return root, data


def find(root, ident, tag):
    items = [e for e in root.iter() if e.get("id") == ident and local(e.tag) == tag]
    if len(items) != 1:
        raise ValueError(f"Expected exactly one {tag} with ID {ident}")
    return items[0]


def href_key(el):
    keys = [k for k in el.attrib if local(k) == "href"]
    if len(keys) != 1:
        raise ValueError("Expected one image href attribute")
    return keys[0]


def protected_digest(root, layer, field=None):
    protected = copy.deepcopy(root)
    image = find(protected, layer, "image")
    image.set(href_key(image), "AUTHORIZED_PORTRAIT")
    if field:
        text = find(protected, field, "text")
        text.text = "AUTHORIZED_NAME"
        for key in ("font-size", "letter-spacing"):
            text.attrib.pop(key, None)
    return sha(ET.tostring(protected, encoding="utf-8"))


def write_new(filename, data):
    target = Path(filename)
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("xb") as stream:
        stream.write(data)


def replace(template, layer, portrait, out, field=None, value=None, font_size=None, letter_spacing=None):
    root, original = load_template(template)
    if (field is None) != (value is None):
        raise ValueError("Provide both field and value, or neither")
    if field is None and (font_size is not None or letter_spacing is not None):
        raise ValueError("Typography changes require an explicit text field")
    if Path(out).exists():
        raise FileExistsError(f"Output exists; choose a new version: {out}")
    before = protected_digest(root, layer, field)
    portrait_bytes = Path(portrait).read_bytes()
    mime = raster_type(portrait_bytes)
    image = find(root, layer, "image")
    image.set(href_key(image), f"data:image/{mime};base64," + base64.b64encode(portrait_bytes).decode("ascii"))
    if field:
        node = find(root, field, "text")
        if len(node):
            raise ValueError("Nested text/tspan field needs a dedicated editable-template workflow")
        if not value.strip() or any(c in value for c in "\r\n\x00"):
            raise ValueError("Name must be a nonempty single line")
        node.text = value
        if font_size is not None:
            if not 8 <= font_size <= 200:
                raise ValueError("Font size must be 8..200 SVG units")
            node.set("font-size", f"{font_size:g}")
        if letter_spacing is not None:
            if not 0 <= letter_spacing <= 15:
                raise ValueError("Letter spacing must be 0..15 SVG units")
            node.set("letter-spacing", f"{letter_spacing:g}")
    after = protected_digest(root, layer, field)
    if after != before:
        raise ValueError("Protected template structure changed")
    result = ET.tostring(root, encoding="utf-8", xml_declaration=True)
    write_new(out, result)
    if sha(Path(out).read_bytes()) != sha(result):
        raise IOError("Output readback mismatch")
    return {
        "output": str(Path(out).resolve()), "source_sha256": sha(original),
        "portrait_sha256": sha(portrait_bytes), "output_sha256": sha(result),
        "protected_sha256": before, "protected_structure_unchanged": True,
        "changed_layer": layer, "changed_text_field": field,
        "visual_qa": "required; structural equality does not prove portrait identity or background fidelity"
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["inspect", "extract", "replace"])
    parser.add_argument("--template", required=True)
    parser.add_argument("--layer")
    parser.add_argument("--out")
    parser.add_argument("--portrait")
    parser.add_argument("--field")
    parser.add_argument("--value")
    parser.add_argument("--font-size", type=float)
    parser.add_argument("--letter-spacing", type=float)
    args = parser.parse_args()
    root, data = load_template(args.template)
    if args.command == "inspect":
        images, texts = [], []
        for el in root.iter():
            if local(el.tag) == "image" and el.get("id"):
                raw = decode_image(el.get(href_key(el)))
                images.append({"id": el.get("id"), "type": raster_type(raw), "bytes": len(raw),
                               "placement": {k: el.get(k) for k in ("x", "y", "width", "height", "preserveAspectRatio")}})
            if local(el.tag) == "text" and el.get("id"):
                texts.append({"id": el.get("id"), "text": "".join(el.itertext()), "simple_field": not len(el)})
        result = {"source_sha256": sha(data), "canvas": {k: root.get(k) for k in ("width", "height", "viewBox")}, "images": images, "texts": texts}
    elif args.command == "extract":
        if not args.layer or not args.out:
            parser.error("extract needs --layer and --out")
        el = find(root, args.layer, "image")
        raw = decode_image(el.get(href_key(el)))
        extension = Path(args.out).suffix.lower()
        allowed = {"png": [".png"], "jpeg": [".jpg", ".jpeg"], "webp": [".webp"]}
        if extension not in allowed[raster_type(raw)]:
            raise ValueError("Output extension must match embedded image type")
        write_new(args.out, raw)
        result = {"output": str(Path(args.out).resolve()), "sha256": sha(raw), "bytes": len(raw)}
    else:
        if not args.layer or not args.portrait or not args.out:
            parser.error("replace needs --layer, --portrait and --out")
        result = replace(args.template, args.layer, args.portrait, args.out, args.field, args.value, args.font_size, args.letter_spacing)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, ET.ParseError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        sys.exit(1)
