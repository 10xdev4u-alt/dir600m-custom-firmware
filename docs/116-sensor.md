# Sensor Integration

## Overview
Connect sensors (temperature, humidity, motion) via GPIO/I2C/SPI.
Log data and serve via HTTP/MQPT.

## Hardware
- I2C sensors (BME280, BMP180)
- SPI sensors (MCP3008 ADC)
- 1-Wire sensors (DS18B20)
- PIR motion sensors (GPIO)

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
- HTTP API for custom scripts
- Grafana for visualization

## Notes
- Level shifters may be needed (3.3V)
- Limited GPIO available
- External ADC for analog sensors
