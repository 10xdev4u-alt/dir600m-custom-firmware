# NAND Flash Information

## Chip
- SPI NOR flash (not NAND)
- 4 MB (32 Mbit)
- 4KB erase sectors
- 256 byte pages

## Access
- /dev/mtd0: entire flash
- /dev/mtd1: kernel
- /dev/mtd2: rootfs
- /dev/mtd3: rootfs_data
- /dev/mtd4: config

## Tools
- flashcp: write to flash
- nanddump: read flash
- mtd: OpenWrt MTD tool
- dd: raw read/write

## Wear Leveling
- Limited on SPI NOR
- Use for read-mostly data
- Avoid frequent writes
