# Troubleshooting

## Build fails with glibc errors
- Use Ubuntu 12.04/14.04 host
- Or patch host tools (see docs/10-host-patching.md)

## Kernel won't boot
- Check UART output (115200 8N1)
- Verify TFTP flash completed
- Try recovery mode (hold reset on power-on)

## WiFi not working
- Check rtl8192cd module loaded
- Verify firmware files present
- Check /etc/config/wireless

## Out of space
- 4MB flash is tight
- Remove unnecessary packages
- Use minimal profile
