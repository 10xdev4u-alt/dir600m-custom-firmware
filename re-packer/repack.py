#!/usr/bin/env python3
"""Re-pack a D-Link DIR-600M C1 web image (.img).

Container format (reverse-engineered):
  header 64 bytes: "DIR600M" + size-ish + date + "router.img"
  body: concatenated LZMA-alone streams, each prefixed by magic 5d 00 00 80 00
        followed by 8-byte uncompressed size (little-endian).

Usage:
  python3 repack.py extract firmware.img outdir/
  python3 repack.py build outdir/ new.img
"""
import sys, os, lzma, struct, glob

MAGIC = b'\x5d\x00\x00\x80\x00'
HEADER_LEN = 0x47  # LZMA stream 0 starts here

def extract(img_path, outdir):
    data = open(img_path, 'rb').read()
    os.makedirs(outdir, exist_ok=True)
    # save header
    open(os.path.join(outdir, 'header.bin'), 'wb').write(data[:HEADER_LEN])
    # carve streams
    pos = HEADER_LEN
    idx = 0
    while pos < len(data):
        i = data.find(MAGIC, pos)
        if i < 0:
            break
        d = lzma.LZMADecompressor(format=lzma.FORMAT_ALONE)
        out = d.decompress(data[i:])
        consumed = len(data[i:]) - len(d.unused_data)
        open(os.path.join(outdir, f'stream_{idx:02d}.bin'), 'wb').write(out)
        print(f'stream {idx:02d}: offset {hex(i)} -> {len(out)} bytes')
        idx += 1
        pos = i + consumed
    print(f'extracted {idx} streams into {outdir}')

def build(outdir, out_img):
    header = open(os.path.join(outdir, 'header.bin'), 'rb').read()
    streams = sorted(glob.glob(os.path.join(outdir, 'stream_*.bin')))
    body = b''
    for s in streams:
        raw = open(s, 'rb').read()
        # LZMA alone: properties + dict size (5 bytes) + 8-byte size + compressed
        c = lzma.compress(raw, format=lzma.FORMAT_ALONE, filters=[{'id': lzma.FILTER_LZMA1, 'dict_size': 1 << 23}])
        # verify magic
        assert c[:5] == MAGIC, f'{s}: bad magic {c[:5].hex()}'
        body += c
        print(f'{os.path.basename(s)}: {len(raw)} -> {len(c)}')
    open(out_img, 'wb').write(header + body)
    print(f'wrote {out_img} ({len(header)+len(body)} bytes)')

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print(__doc__); sys.exit(1)
    if sys.argv[1] == 'extract':
        extract(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == 'build':
        build(sys.argv[2], sys.argv[3])
    else:
        print('unknown command'); sys.exit(1)
