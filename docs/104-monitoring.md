# System Monitoring

## Overview
Track system health, performance, and security.

## Tools
- top: CPU/memory usage
- logread: system log
- cat /proc/meminfo: memory details
- cat /proc/cpuinfo: CPU info
- ifstat: network throughput
- vnstat: traffic statistics

## Alerts
- /etc/init.d/monitor
- Check disk usage, memory, CPU
- Send alert via SSH or email
- Log to /var/log/monitor.log

## Graphs
- collectd + rrdtool
- luci-app-statistics
- Export to external monitoring (Grafana)

## Notes
- 32 MB RAM limits monitoring tools
- Use lightweight tools only
- External monitoring preferred
