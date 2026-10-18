# Realtek Bootloader

## Overview
- Proprietary Realtek bootloader
- Located at 0x000000-0x030000 in flash
- Version: v1.1c (16bit, 390MHz)

## Boot Sequence
1. Bootloader initializes hardware
2. Checks for TFTP recovery mode (reset button held)
3. Loads kernel from flash to 0x80500000
4. Decompresses kernel to 0x80000000
5. Jumps to kernel entry point

## Recovery Mode
- Triggered by holding reset button on power-on
- Router gets IP 192.168.1.6
- Waits for TFTP upload
- Burns kernel to 0x30000, rootfs to 0x1b0000

## UART Output
- Boot messages at 115200 baud
- Shows hardware init, memory test
- Recovery mode: "TFTP Client Upload" messages
