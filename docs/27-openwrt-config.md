# OpenWrt Configuration for RTL8196C

## Target
- Target System: Realtek RTL8196C
- Subtarget: rtl8196c
- Profile: nprove

## Kernel
- Version: 2.6.30.9
- Config: target/linux/realtek/config-2.6.30

## Packages (nprove profile)
- kmod-tun, kmod-nls-*, kmod-fs-vfat
- kmod-usb-ohci, kmod-usb-uhci, kmod-usb2
- kmod-usb-serial, kmod-usb-storage
- luci, luci-app-diag-devinfo
- firewall, block-mount, qos-scripts

## Flash
- Kernel offset: 0x30000
- Rootfs offset: 0x1b0000
- Total image: ~1.4MB (fits in 4MB)
