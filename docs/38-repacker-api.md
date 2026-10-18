# Re-Packer API Reference

## extract(img_path, outdir)
Extracts all LZMA streams from firmware image.
- img_path: Path to .img file
- outdir: Output directory for streams

## build(outdir, out_img)
Rebuilds firmware image from extracted streams.
- outdir: Directory containing stream_*.bin files
- out_img: Output .img file path

## Constants
- MAGIC = b'\x5d\x00\x00\x80\x00'
- HEADER_LEN = 0x47

## Usage Example
```python
import repack
repack.extract('firmware.img', 'streams/')
# edit streams/stream_00.bin
repack.build('streams/', 'new.img')
```
