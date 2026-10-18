# 3G/4G Modem Support

## Hardware
- USB port (if present on PCB)
- Huawei E173, E1750, E3131 common
- kmod-usb-serial-option for modem

## Configuration
- /etc/config/network:
```
config interface '3g'
    option ifname '3g'
    option proto '3g'
    option service 'umts'
    option apn 'internet'
    option device '/dev/ttyUSB2'
```

## Setup
1. Connect modem to USB
2. Install kmod-usb-serial-option
3. Configure APN
4. Start interface
5. Monitor with logread

## Notes
- Power may be limited
- Use powered hub for some modems
- Check dmesg for device detection
