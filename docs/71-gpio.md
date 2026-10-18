# GPIO on DIR-600M

## Overview
General Purpose I/O pins available for user programs.
LEDs, buttons, and external circuits.

## GPIO Pins
- GPIO0-27: general purpose (multiplexed)
- GPIO28-31: reserved

## LED Pins
- Power LED: GPIO0 (green)
- WLAN LED: GPIO1 (green)
- WAN LED: GPIO2 (green)
- LAN LEDs: GPIO3-6 (green)

## Button Pins
- Reset: GPIO7 (active low)
- WPS: GPIO8 (active low)

## Usage
- echo 1 > /sys/class/gpio/gpio0/value
- echo out > /sys/class/gpio/gpio0/direction
- cat /sys/class/gpio/gpio7/value
