# Re-Packer Internals

## Extract
- Read firmware.img
- Header = first 0x47 bytes
- Find MAGIC (5d 00 00 80 00) in body
- LZMA-decompress each stream (FORMAT_ALONE)
- Track consumed bytes via unused_data
- Save as stream_XX.bin

## Build
- Read header.bin
- For each stream_XX.bin:
  - LZMA compress with dict_size=8MB (1<<23)
  - Verify magic matches
- Concatenate all compressed streams
- Write header + body to output

## Verification
- Extract rebuilt image
- Compare all streams byte-for-byte
- All 28 streams round-trip identically
