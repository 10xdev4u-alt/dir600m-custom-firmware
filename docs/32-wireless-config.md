# Wireless Configuration

## Driver
- rtl8192cd (Realtek proprietary)
- Kernel module: rtl8192cd.ko
- Firmware: rtl8192cfw.bin, rtl8192cfwn.bin

## Configuration
/etc/config/wireless:
```
config wifi-device radio0
    option type mac80211
    option channel 6
    option hwmode 11n
    option path 'platform/rtl8192cd'

config wifi-iface
    option device radio0
    option network lan
    option mode ap
    option ssid DIR-600M
    option encryption psk2
    option key password
```

## Notes
- 2.4 GHz only
- 802.11n 150 Mbps
- WPA2-PSK supported
