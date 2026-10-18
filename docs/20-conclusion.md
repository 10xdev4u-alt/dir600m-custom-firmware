# Conclusion

## What we achieved
- Reverse-engineered firmware container format
- Built re-packer for web image modification
- Mapped all CVEs and attack surface
- Located OpenWrt port and toolchain
- Documented hardware constraints

## What's next
- Flash v3.08 and harden
- Set up VM for OpenWrt build
- TFTP flash custom firmware
- Experiment with UART

## The deep game
Custom firmware for RTL8196C is possible but requires:
- Old host toolchain (Ubuntu 12.04/14.04)
- Realtek SDK patches
- Wireless driver integration
- 4MB flash constraint management
