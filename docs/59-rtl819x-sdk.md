# RTL819x SDK Overview

## Realtek SDK Versions
- v2.5.2: Original (2010)
- v3.4.6.2: Updated (2016)
- v4.4.7: Latest (2017)

## Components
- Toolchain: gcc + binutils for mips-linux-uclibc
- Kernel: 2.6.30/2.6.32 with Realtek patches
- Rootfs: uClibc + busybox
- Applications: goahead (web server), hostapd, dnsmasq

## Directory Structure
```
rtl819x-sdk/
├── toolchain/     # gcc, binutils
├── linux/         # kernel source
├── rootfs/        # base filesystem
├── applications/  # user programs
└── tools/         # build tools (cvimg, etc.)
```

## License
- Proprietary (Realtek)
- Not open source (toolchain binaries only)
- Kernel patches GPL
