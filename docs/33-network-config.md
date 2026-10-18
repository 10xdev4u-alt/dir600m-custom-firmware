# Network Configuration

## Default IP
- LAN: 192.168.0.1
- Recovery: 192.168.1.6

## Interfaces
- eth0: WAN
- eth1-4: LAN
- wlan0: Wireless

## /etc/config/network
```
config interface 'lan'
    option type bridge
    option ifname 'eth1 eth2 eth3 eth4 wlan0'
    option proto static
    option ipaddr 192.168.0.1
    option netmask 255.255.255.0

config interface 'wan'
    option ifname 'eth0'
    option proto dhcp
```

## DHCP
- Range: 192.168.0.100-192.168.0.200
- Lease: 12h
