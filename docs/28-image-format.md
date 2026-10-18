# OpenWrt Image Format for Realtek

## Kernel Image
- Format: gzip-compressed vmlinux
- File: openwrt-realtek-rtl8196c-nprove-kernel.bin
- Load address: 0x80500000
- Entry: 0x80003530

## Rootfs Image
- Format: SquashFS 4.0
- File: openwrt-realtek-rtl8196c-nprove-squashfs.bin
- Burned to: 0x1b0000

## Sysupgrade Image
- Combined kernel + rootfs
- File: openwrt-realtek-rtl8196c-nprove-sysupgrade.img

## cvimg Tool
- Used to create bootable images
- Adds checksums and headers
- Part of Realtek SDK
