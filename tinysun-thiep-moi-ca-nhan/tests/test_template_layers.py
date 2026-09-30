import base64
import importlib.util
import tempfile
import unittest
from pathlib import Path

script = Path(__file__).resolve().parents[1] / "scripts" / "template_layers.py"
spec = importlib.util.spec_from_file_location("layers", script)
layers = importlib.util.module_from_spec(spec)
spec.loader.exec_module(layers)
PNG = base64.b64decode("iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+aZ1cAAAAASUVORK5CYII=")
SVG = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="100" height="200"><rect fill="#fff" width="100" height="200"/><image id="portrait" x="1" y="2" width="40" height="60" xlink:href="data:image/png;base64,{base64.b64encode(PNG).decode()}"/><text id="guest" x="50" y="100" font-size="20">QUÝ ĐỐI TÁC</text><text id="event" x="50" y="150">VIETBABY · 15–18.10.2026</text></svg>'''


class TestLayers(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.template = self.root / "source.svg"
        self.template.write_text(SVG, encoding="utf-8")
        self.portrait = self.root / "portrait.png"
        self.portrait.write_bytes(PNG)
        self.output = self.root / "new.svg"

    def test_only_authorized_field_changes_source_is_preserved(self):
        original = self.template.read_bytes()
        result = layers.replace(self.template, "portrait", self.portrait, self.output, "guest", "NGUYỄN ANH & BÉ <VIP>", 18, 1)
        before, _ = layers.load_template(self.template)
        after, _ = layers.load_template(self.output)
        self.assertTrue(result["protected_structure_unchanged"])
        self.assertEqual(layers.protected_digest(before, "portrait", "guest"), layers.protected_digest(after, "portrait", "guest"))
        self.assertEqual(layers.find(after, "guest", "text").text, "NGUYỄN ANH & BÉ <VIP>")
        self.assertEqual(layers.find(after, "event", "text").text, "VIETBABY · 15–18.10.2026")
        self.assertEqual(self.template.read_bytes(), original)

    def test_name_optional(self):
        layers.replace(self.template, "portrait", self.portrait, self.output)
        after, _ = layers.load_template(self.output)
        self.assertEqual(layers.find(after, "guest", "text").text, "QUÝ ĐỐI TÁC")

    def test_no_overwrite(self):
        self.output.write_bytes(b"keep")
        with self.assertRaises(FileExistsError):
            layers.replace(self.template, "portrait", self.portrait, self.output)
        self.assertEqual(self.output.read_bytes(), b"keep")

    def test_unknown_id_no_output(self):
        with self.assertRaises(ValueError):
            layers.replace(self.template, "unknown", self.portrait, self.output)
        self.assertFalse(self.output.exists())

    def test_duplicate_id(self):
        self.template.write_text(SVG.replace('id="event"', 'id="guest"'), encoding="utf-8")
        with self.assertRaises(ValueError):
            layers.load_template(self.template)

    def test_external_image_rejected(self):
        self.template.write_text(SVG.replace('data:image/png;base64,' + base64.b64encode(PNG).decode(), 'https://example.org/image.png'), encoding="utf-8")
        with self.assertRaises(ValueError):
            layers.load_template(self.template)

    def test_script_rejected(self):
        self.template.write_text(SVG.replace('</svg>', '<script>alert(1)</script></svg>'), encoding="utf-8")
        with self.assertRaises(ValueError):
            layers.load_template(self.template)

    def test_wrong_image_signature(self):
        self.portrait.write_bytes(b"not a picture")
        with self.assertRaises(ValueError):
            layers.replace(self.template, "portrait", self.portrait, self.output)

    def test_no_typography_without_field(self):
        with self.assertRaises(ValueError):
            layers.replace(self.template, "portrait", self.portrait, self.output, font_size=12)

    def test_multiline_name_rejected(self):
        with self.assertRaises(ValueError):
            layers.replace(self.template, "portrait", self.portrait, self.output, "guest", "A\nB")


if __name__ == "__main__":
    unittest.main()
