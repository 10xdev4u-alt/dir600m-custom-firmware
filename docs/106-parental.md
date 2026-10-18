# Parental Controls

## Overview
Restrict internet access for specific devices.
Time-based and content-based.

## MAC Filtering
- /etc/config/wireless:
```
config wifi-iface
    option macfilter 'allow'
    option maclist 'AA:BB:CC:DD:EE:FF'
```

## Time Restrictions
- /etc/config/firewall:
```
config rule
    option name 'Block-Kids-Evening'
    option src 'lan'
    option src_mac 'AA:BB:CC:DD:EE:FF'
    option start_time '20:00'
    option stop_time '07:00'
    option target 'REJECT'
```

## DNS Filtering
- Use family-friendly DNS:
  - 208.67.222.123, 208.67.220.123 (OpenDNS Family)
  - 9.9.9.9 (Quad9)
