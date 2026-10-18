# Bootloader Hacks

## Boot Args
- Append to kernel cmdline via bootloader
- console=ttyS0,115200
- root=/dev/mtdblock4
- init=/bin/sh (single user)

## Recovery TFTP
- Triggered by reset button hold
- Router at 192.168.1.6
- Burns to 0x30000 (kernel) and 0x1b0000 (rootfs)

## Boot from UART
- Send 'b' at boot prompt
- Load kernel via TFTP
- Useful for testing without flashing

## NAND Bad Blocks
- Check with nanddump
- Mark bad blocks
- Avoid writing to bad blocks
