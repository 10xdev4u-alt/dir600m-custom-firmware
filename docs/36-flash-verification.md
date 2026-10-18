# Flash Verification

## After TFTP Flash
1. Check UART output for success messages
2. Wait for router to reboot (30-60 seconds)
3. Check for new SSID (OpenWrt default)
4. Try SSH: ssh root@192.168.1.1
5. Check UCI: uci show network

## Recovery if Failed
1. Power off router
2. Hold reset, power on
3. Re-enter TFTP recovery
4. Re-flash original firmware

## Common Issues
- Wrong image for hardware revision
- Corrupted download (verify md5)
- TFTP timeout (check firewall)
- Wrong IP address (must be 192.168.1.x)

## Verification Commands
- ifconfig: check interfaces
- dmesg: kernel messages
- logread: system log
- wifi detect: wireless status
