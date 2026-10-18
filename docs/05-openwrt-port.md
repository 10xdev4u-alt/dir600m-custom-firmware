# OpenWrt Port for RTL8196C

## Status: Community port exists, not mainline

### Repos
- hkwi/openwrt-realtek (branch: realtek) - OpenWrt fork, 2.6.30 kernel
- utessel/edimax - more complete, includes wireless drivers (rtl8192cd)
- hackpascal/lede-rtl8196c - LEDE port, no wireless
- AlexeySofree/openwrt-rtl819x - Barrier Breaker-based

### Toolchain
- gcc 4.5-linaro + binutils 2.21.1 (hacked for Lexra)
- Kernel 2.6.30/2.6.32 from Realtek SDK
- uClibc

### Build on modern host: BLOCKED
- glibc 2.38 incompatibilities in host tools
- Requires old host (Ubuntu 12.04/14.04) or extensive patching

### Flash method
- TFTP to 192.168.1.6 (bootloader recovery mode)
- Upload kernel.bin then squashfs.bin
- UART for debugging (115200 8N1)
