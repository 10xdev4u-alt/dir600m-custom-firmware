# Relay Control

## Overview
Control relays (lights, motors, appliances) via GPIO.
Useful for home automation.

## Hardware
- Relay module (5V, active low/high)
- Connected to GPIO pins
- External 5V power supply

## Software
- Direct GPIO control:
```
echo 1 > /sys/class/gpio/gpio0/value
```
- Lua script:
```lua
local gpio = 0
local val = arg[1] == "on" and 1 or 0
fs.write("/sys/class/gpio/gpio" .. gpio .. "/value", tostring(val))
```

## Safety
- Use opto-isolated relays
- External power for relays
- Fuse protection
- Proper enclosure

## Notes
- GPIO pins are 3.3V
- Relay module may need level shifter
- Active low vs active high check
