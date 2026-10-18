# TFTP Flash Procedure for DIR-600M

## Recovery Mode
1. Power off router
2. Hold reset button
3. Power on, keep holding reset for ~10s
4. Router enters recovery mode at 192.168.1.6

## Flash Sequence
1. Set PC IP to 192.168.1.2/24
2. Start TFTP server
3. Upload kernel: openwrt-realtek-rtl8196c-nprove-kernel.bin
4. Upload rootfs: openwrt-realtek-rtl8196c-nprove-squashfs.bin
5. Router reboots into OpenWrt

## UART Debug
- 4-pin header on PCB
- 115200 baud, 8N1
- TX/RX/GND/VCC
