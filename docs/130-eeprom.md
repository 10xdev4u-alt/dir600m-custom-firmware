# EEPROM Support

## Overview
Non-volatile memory for configuration storage.
I2C or SPI interface.

## Hardware
- 24C256 (I2C, 32KB)
- 25LC256 (SPI, 32KB)
- 24C02 (I2C, 256 bytes)

## Software
- I2C:
```
opkg install kmod-i2c-dev
cat /sys/bus/i2c/devices/0-0050/eeprom
```

## Usage
- Configuration storage
- Calibration data
- Device ID
- Firmware parameters

## Notes
- Write endurance: 1M cycles
- Page write (64 bytes)
- Write protect pin
- 3.3V logic
