# Weather Station

## Overview
Connect weather sensors to the router.
Log data and serve via HTTP/MQTT.

## Hardware
- I2C/SPI sensors (BME280, DHT22)
- ADC for analog sensors
- USB-to-I2C adapter

## Software
- node-red:
```
opkg install node-red
node-red &
```
- Configure flows to read sensors
- Log to file or MQTT

## Integration
- Home Assistant via MQTT
- Weather Underground upload
- Local web dashboard

## Notes
- Sensors may need level shifter (3.3V)
- Limited GPIO available
- External ADC recommended
