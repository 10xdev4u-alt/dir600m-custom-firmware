# UART Troubleshooting

## No Output on UART
- Check baud rate (115200)
- Verify TX/RX not swapped
- Check GND connection
- Try different USB-TTL adapter
- Check if UART is enabled in bootloader

## Garbled Output
- Wrong baud rate (try 9600, 57600)
- Bad ground connection
- Too long wires
- Power supply noise

## Router Won't Boot
- Check UART for error messages
- Try TFTP recovery
- Verify power supply (12V 1A)
- Check for physical damage
- Look for burnt components

## Recovery Mode Not Working
- Hold reset longer (15-30s)
- Try different reset button
- Check if bootloader is corrupted
- May need JTAG or chip-off
