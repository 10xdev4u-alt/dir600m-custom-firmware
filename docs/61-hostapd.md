# hostapd Configuration

## Overview
Host Access Point Daemon
Used in OpenWrt for wireless AP mode.

## Realtek Version
- hostapd-rtk (Realtek's fork)
- Patched for rtl8192cd driver
- Supports WPA/WPA2

## Configuration
/etc/config/wireless:
```
config wifi-device radio0
    option type mac80211
    option channel 6
    option hwmode 11n

config wifi-iface
    option device radio0
    option network lan
    option mode ap
    option ssid MyNetwork
    option encryption psk2
    option key mypassword
```

## Notes
- Realtek's hostapd fork is required
- Standard hostapd doesn't work with rtl8192cd
- WPA3 not supported
