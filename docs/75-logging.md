# System Logging

## logd (OpenWrt)
- Central logging daemon
- Collects messages from all services
- Writes to ring buffer or file

## Usage
- logread: display logs
- logread -f: follow logs (tail -f)
- logread | grep error: filter errors
- logger "message": log a message

## Remote Logging
- /etc/config/system:
```
config system
    option log_ip '192.168.1.100'
    option log_port '514'
    option log_proto 'udp'
```

## Rotation
- /etc/logrotate.conf
- Automatic rotation to prevent fill
