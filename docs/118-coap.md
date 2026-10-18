# CoAP Protocol

## Overview
Constrained Application Protocol for low-power devices.
UDP-based, lightweight alternative to HTTP.

## Hardware
- CoAP sensors/actuators
- UDP communication
- Low power

## Software
- libcoap:
```
opkg install libcoap
coap-client -m get coap://192.168.0.100/temperature
```

## Methods
- GET: read
- POST: create/update
- PUT: replace
- DELETE: remove

## Integration
- Home Assistant via MQTT bridge
- HTTP proxy for web access
- Direct CoAP client apps

## Notes
- UDP (unreliable, but lightweight)
- DTLS for security
- Observe for subscriptions
