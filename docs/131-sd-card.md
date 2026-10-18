# SD Card Support

## Overview
SD/MMC card for expanded storage.
SPI or SDIO interface.

## Hardware
- SD card slot (if present on PCB)
- SD-to-SPI adapter
- SD card (FAT32 or ext4)

## Software
- kmod-mmc-core
- kmod-mmc-spi (SPI interface)
- kmod-sdhost (SDIO interface)

## Usage
- Storage expansion
- Data logging
- Firmware backup
- Media server

## Notes
- Check if SD slot exists on PCB
- 3.3V logic
- FAT32 for compatibility
- ext4 for Linux
