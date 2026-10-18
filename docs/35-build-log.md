# Build Log Summary

## Attempt 1: hkwi/openwrt-realtek
- Host: Arch Linux (glibc 2.38)
- Result: Blocked at host tools
- Patches applied: m4, pkg-config, bison, mklibs
- Remaining: cmake, e2fsprogs, gdb, mkimage

## Attempt 2: utessel/edimax
- Same host
- Result: Same blockers
- External toolchain configured
- Kernel patches applied manually

## Conclusion
- Modern host not suitable for 2013-era OpenWrt build
- Need Ubuntu 12.04/14.04 host
- All patches and workarounds documented
