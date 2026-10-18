# SquashFS Filesystem

## Overview
Read-only compressed filesystem used for the rootfs partition.

## Features
- LZMA/XZ/GZIP compression
- High compression ratio (~50%)
- Fast random access
- No write support (by design)

## Creation
```
mksquashfs rootfs/ rootfs.squashfs \
  -comp xz \
  -b 131072 \
  -noappend \
  -all-root
```

## Size
- OpenWrt nprove: ~700KB
- Fits in 0x130000-0x3F0000 (2.5MB) partition

## Verification
```
unsquashfs -s rootfs.squashfs
```
