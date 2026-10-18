# Power Management

## Power Supply
- Input: 12V DC, 1A
- Consumption: ~2-3W typical
- Idle: ~1.5W
- Peak: ~4W

## Power Control
- GPIO-controlled regulators
- USB power switch (GPIO)
- Wireless power switch (GPIO)

## Sleep Modes
- CPU sleep (idle)
- Peripheral power-down
- Wake-on-LAN (if supported)
- Wake-on-GPIO

## Monitoring
- /sys/class/power_supply/ (if ADC present)
- Voltage monitoring via GPIO ADC
- Current monitoring (rare)
