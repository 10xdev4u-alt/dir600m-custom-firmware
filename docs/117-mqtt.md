# MQTT Protocol

## Overview
Lightweight publish-subscribe messaging protocol.
Ideal for IoT and home automation.

## Broker (mosquitto)
```
opkg install mosquitto mosquitto-client
/etc/init.d/mosquitto start
```

## Publish
```
mosquitto_pub -h localhost -t "sensors/temperature" -m "25.5"
```

## Subscribe
```
mosquitto_sub -h localhost -t "sensors/#"
```

## Topics
- sensors/temperature
- sensors/humidity
- actuators/light
- status/online

## QoS
- 0: at most once (fire and forget)
- 1: at least once (acknowledged)
- 2: exactly once (guaranteed)
