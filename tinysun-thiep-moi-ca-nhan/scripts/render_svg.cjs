// Raster export only. Portrait generation must be done with image_gen first.
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');

function parseArgs(argv) {
  const args = {};
  for (let i = 0; i < argv.length; i += 2) {
    if (!['--svg', '--out', '--modules'].includes(argv[i]) || !argv[i + 1]) throw new Error('Expected --svg FILE --out NEW_STEM [--modules NODE_MODULES]');
    if (args[argv[i]]) throw new Error('Duplicate option');
    args[argv[i]] = argv[i + 1];
  }
  if (!args['--svg'] || !args['--out']) throw new Error('--svg and --out are required');
  return args;
}

function checkStaticSvg(text) {
  if (/<!DOCTYPE|<!ENTITY|<\?xml-stylesheet|@import|@font-face|<(?:\w+:)?(?:script|foreignObject|animate\w*|set)\b|\son\w+\s*=|xml:base/i.test(text)) throw new Error('Unsupported dynamic/external SVG');
  for (const match of text.matchAll(/(?:[\w-]+:)?href\s*=\s*(["'])(.*?)\1/gs)) {
    if (!/^(?:#[\w.-]+|data:image\/(?:png|jpeg|webp);base64,[A-Za-z0-9+/=\s]+)$/.test(match[2])) throw new Error('Only embedded raster images and local fragment href are allowed');
  }
  for (const match of text.matchAll(/url\s*\(([^)]*)\)/gi)) {
    if (!/^[\s"']*#[\w.-]+[\s"']*$/.test(match[1])) throw new Error('External CSS URL is unsupported');
  }
  if (text.includes('\\')) throw new Error('Escaped SVG/CSS needs review');
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  const mod = args['--modules'];
  const sharp = require(mod ? require.resolve('sharp', {paths: [path.resolve(mod)]}) : 'sharp');
  const source = fs.readFileSync(args['--svg']);
  checkStaticSvg(source.toString('utf8'));
  const stem = path.resolve(args['--out']);
  const targets = ['.png', '.jpg', '-preview.png', '-render.json'].map(x => stem + x);
  for (const target of targets) if (fs.existsSync(target)) throw new Error('Output already exists: ' + target);
  const input = sharp(source, {limitInputPixels: 60000000});
  const metadata = await input.metadata();
  if (!metadata.width || !metadata.height) throw new Error('SVG dimensions missing');
  const png = await input.png().toBuffer();
  const jpg = await sharp(png).flatten({background: '#ffffff'}).jpeg({quality: 95, chromaSubsampling: '4:4:4'}).toBuffer();
  const preview = await sharp(png).resize({width: Math.min(720, metadata.width)}).png().toBuffer();
  const blobs = [png, jpg, preview];
  fs.mkdirSync(path.dirname(stem), {recursive: true});
  for (let i = 0; i < blobs.length; i++) fs.writeFileSync(targets[i], blobs[i], {flag: 'wx'});
  const digest = buffer => crypto.createHash('sha256').update(buffer).digest('hex');
  const manifest = {
    source: path.resolve(args['--svg']), source_sha256: digest(source),
    width: metadata.width, height: metadata.height,
    files: targets.slice(0, 3).map((file, i) => ({file, bytes: blobs[i].length, sha256: digest(blobs[i])})),
    visual_qa: 'required; this renderer does not verify the guest face, hands or invitation facts'
  };
  fs.writeFileSync(targets[3], JSON.stringify(manifest, null, 2), {flag: 'wx'});
  for (let i = 0; i < blobs.length; i++) if (digest(fs.readFileSync(targets[i])) !== digest(blobs[i])) throw new Error('Readback mismatch');
  console.log(JSON.stringify(manifest, null, 2));
}

main().catch(error => { console.error(error.message); process.exitCode = 1; });
