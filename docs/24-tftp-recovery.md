# TFTP Recovery Mode Details

## Entering Recovery
1. Power off router
2. Hold reset button
3. Power on
4. Keep holding reset for 10-15 seconds
5. Router boots into recovery at 192.168.1.6

## Network Setup
- PC IP: 192.168.1.2
- Netmask: 255.255.255.0
- Gateway: 192.168.1.6

## TFTP Server
- Linux: atftpd or tftp-hpa
- Windows: tftpd32
- Place kernel.bin and squashfs.bin in TFTP root

## Flash Order
1. kernel.bin (burns to 0x30000)
2. squashfs.bin (burns to 0x1b0000)

## Verification
- UART output shows progress
- Router reboots automatically
