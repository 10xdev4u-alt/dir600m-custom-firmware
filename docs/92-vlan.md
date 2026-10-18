# VLAN Configuration

## Overview
Virtual LANs for network segmentation.
DIR-600M has 5 Ethernet ports (1 WAN + 4 LAN).

## /etc/config/network
```
config switch
    option name 'switch0'
    option reset '1'
    option enable_vlan '1'

config switch_vlan
    option device 'switch0'
    option vlan '1'
    option ports '0 1 2 3 5t'

config switch_vlan
    option device 'switch0'
    option vlan '2'
    option ports '4 5t'
```

## Notes
- Port 5 is CPU (internal)
- VLAN 1 = LAN
- VLAN 2 = WAN
