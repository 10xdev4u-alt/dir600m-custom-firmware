# Pre-Built OpenWrt Image for RTL8196C

## Source
- nprove project (Roman Yeryomin)
- Image: openwrt-realtek-rtl8196c-nprove-squashfs.bin + kernel.bin

## Flash
- TFTP to 192.168.1.6
- Upload kernel first, then squashfs
- UART for debug (115200 8N1)

## Note
- Kernel 2.6.30, OpenWrt Barrier Breaker era
- WiFi works (rtl8188re driver)
- Limited package space (4MB flash)
