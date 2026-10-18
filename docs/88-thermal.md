# Thermal Management

## Overview
RTL8196C has internal temperature sensor.
Can be read via sysfs or ADC.

## Temperature Zones
- Normal: < 70°C
- Warm: 70-80°C
- Hot: 80-90°C
- Critical: > 90°C

## Monitoring
- cat /sys/class/thermal/thermal_zone0/temp
- Check dmesg for thermal warnings
- Watch for throttling in logs

## Cooling
- Ensure ventilation
- Avoid enclosed spaces
- Consider heatsink if hot
- Reduce CPU load if overheating
