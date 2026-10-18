# CPU Frequency Scaling

## Overview
RTL8196C supports dynamic frequency scaling for power saving.

## Frequencies
- 390 MHz (full speed)
- 195 MHz (half speed)
- 97 MHz (quarter speed)

## Configuration
- /etc/config/system:
```
config system
    option cpufreq_governor 'ondemand'
    option cpufreq_min '97'
    option cpufreq_max '390'
```

## Usage
- echo 195000000 > /sys/devices/system/cpu/cpu0/cpufreq/scaling_setspeed
- cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq
