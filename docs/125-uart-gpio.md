# UART via GPIO (Bit-Bang)

## Overview
Software UART on GPIO pins.
Useful when hardware UART is occupied.

## Hardware
- Any GPIO pin
- 115200 baud max (reliable)
- Lower baud rates more reliable

## Software
- kernel module:
```
opkg install kmod-softuart
```
- Configure /etc/config/system:
```
config softuart
    option tx '12'
    option rx '13'
    option baud '9600'
```

## Notes
- CPU intensive
- Not reliable at high speeds
- Use hardware UART if possible
- Interrupts may cause errors
