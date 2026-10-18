# JFFS2 Filesystem

## Overview
Journalling Flash File System 2
Used for the rootfs_data partition (writable overlay).

## Features
- Wear leveling
- Compression (LZO, zlib, none)
- Power-loss safe
- Bad block handling

## Configuration
- Block size: 4KB (matches flash erase size)
- Cleanmarkers: 0x2003 (little endian)
- ECC: software (for NAND)

## Mount
```
mount -t jffs2 /dev/mtdblock4 -o noatime /overlay
```

## Maintenance
- jffs2dump: inspect filesystem
- jffs2reader: extract files
- Sumtool: generate summary nodes
