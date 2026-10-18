# utessel/edimax Repository

## Overview
- OpenWrt fork with Realtek target
- Includes wireless drivers (rtl8192cd)
- USB support (ohci/uhci/ehci)
- More complete than hkwi/openwrt-realtek

## Structure
- target/linux/realtek/rtl8196c/ (target config)
- target/linux/realtek/rtl8196c/profiles/nprove.mk (package set)
- target/linux/realtek/patches-2.6.30/ (kernel patches)

## Key packages
- kmod-tun, kmod-usb-*, luci, firewall, block-mount
