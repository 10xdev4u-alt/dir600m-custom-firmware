# Flash Tools

## TFTP (Recovery Mode)
- Linux: atftpd, tftp-hpa
- Windows: tftpd32
- Upload: kernel.bin, squashfs.bin

## DD (Direct Write)
- dd if=firmware.img of=/dev/sdX
- For USB/SD card boot
- Verify with md5sum

## OpenWrt Sysupgrade
- sysupgrade firmware.bin
- Web UI: LuCI -> System -> Backup/Flash
- Command line: sysupgrade -n firmware.bin

## D-Link Web UI
- Administration -> Firmware Update
- Upload .img file
- Wait for reboot (30-60s)

## Safety
- Never power off during flash
- Verify image before flashing
- Keep backup of original
