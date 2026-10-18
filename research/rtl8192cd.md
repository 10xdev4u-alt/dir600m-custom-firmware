# RTL8192CD Wireless Driver

## Overview
- Realtek's proprietary wireless driver
- Included in utessel/edimax fork
- Supports RTL8192C/RTL8192D/RTL8192E
- AP mode supported

## Files
- drivers/net/wireless/rtl8192cd/
- firmware: rtl8192cfw.bin, rtl8192cfwn.bin, rtl8192cfwua.bin

## Integration
- Built as kernel module
- Loaded at boot
- Configured via /etc/config/wireless
