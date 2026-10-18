# Firmware Container Format (Reverse-Engineered)

## Header (64 bytes, offset 0x00-0x46)
- 0x00-0x06: "DIR600M" magic
- 0x07-0x0A: size-ish (a0 00 00 03)
- 0x10-0x13: 12 ef 4c 80
- 0x1A-0x30: date string "Wed May 29 17:36:03 2019\0"
- 0x31-0x3D: "router.img\0"

## Body (offset 0x47+)
- 28 consecutive LZMA-alone streams
- Each: magic 5d 00 00 80 00 + 8-byte LE uncompressed size + compressed data
- Total decompressed: ~893 KB
