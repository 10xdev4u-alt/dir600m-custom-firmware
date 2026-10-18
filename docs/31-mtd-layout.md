# MTD Partition Layout

## 4MB Flash Map
| Offset   | Size     | Partition    |
|----------|----------|--------------|
| 0x000000 | 0x030000 | bootloader   |
| 0x030000 | 0x100000 | kernel       |
| 0x130000 | 0x080000 | rootfs       |
| 0x1B0000 | 0x240000 | rootfs_data  |
| 0x3F0000 | 0x010000 | config       |

## Kernel
- LZMA compressed
- Loaded to 0x80500000

## Rootfs
- SquashFS 4.0
- Read-only

## rootfs_data
- JFFS2
- Read-write overlay

## Config
- NVRAM settings
- MAC addresses
- Calibration data
