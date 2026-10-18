# Cron Jobs

## Overview
Task scheduler for periodic tasks.
Runs cron jobs in /etc/crontabs/

## /etc/crontabs/root
```
# Run backup every night at 3am
0 3 * * * /usr/bin/backup.sh

# Restart network every Monday at 4am
0 4 * * 1 /etc/init.d/network restart

# Check for firmware updates weekly
0 5 * * 0 /usr/bin/check-updates.sh
```

## Enable Cron
- /etc/init.d/cron enable
- /etc/init.d/cron start

## Logs
- logread | grep cron
