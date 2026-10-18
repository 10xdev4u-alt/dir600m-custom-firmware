# cvimg Tool

## Purpose
Creates bootable firmware images for Realtek routers.
Adds checksums and headers that the bootloader expects.

## Usage
```
cvimg root <input.img> <output.bin> F0000 <rootfs_offset>
```

## Parameters
- root: image type
- input.img: raw image file
- output.bin: bootable output
- F0000: flash offset for bootloader
- rootfs_offset: CONFIG_REALTEK_ROOTFS_OFFSET

## Output Files
- kernel.bin: bootable kernel image
- squashfs.bin: bootable rootfs image
- sysupgrade.img: combined kernel + rootfs

## Source
Part of Realtek SDK (tools/cvimg/)
