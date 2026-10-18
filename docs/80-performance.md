# Performance Optimization

## CPU
- 390 MHz Lexra (limited)
- No FPU (soft float)
- Single core

## Memory
- 32 MB RAM (tight)
- Reduce running services
- Use swap on USB (slow)

## Network
- Enable flow offloading
- Reduce conntrack table size
- Limit QoS rules

## Wireless
- Fixed channel (avoid scanning)
- Reduce transmit power if close
- Disable unused features

## Storage
- Use JFFS2 compression
- Reduce log rotation
- Clean /tmp regularly
