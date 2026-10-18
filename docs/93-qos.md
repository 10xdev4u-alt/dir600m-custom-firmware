# QoS (Quality of Service)

## Overview
Traffic shaping to prioritize important traffic.
Useful for VoIP, gaming, streaming.

## Configuration
- luci-app-qos: web UI for QoS
- /etc/config/qos:
```
config interface 'wan'
    option enabled '1'
    option download '10000'
    option upload '5000'

config classify
    option target 'Priority'
    option proto 'tcp'
    option ports '22'
```

## Limits
- QoS on 390 MHz CPU is limited
- Simple rules only
- Test before deploying
