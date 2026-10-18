# Memory Information

## RAM
- 32 MB SDRAM (total)
- 30 MB available to kernel
- 2 MB reserved for firmware

## Usage
- free -h: show memory usage
- cat /proc/meminfo: detailed info
- top: per-process usage

## Optimization
- Reduce buffer sizes
- Use lighter alternatives
- Avoid large log files
- Enable swap on USB (slow but works)

## Limits
- LuCI: ~20 MB
- dnsmasq: ~5 MB
- hostapd: ~10 MB
- Total: tight but workable
