# Backup and Restore

## Backup
- sysupgrade -b /tmp/backup.tar.gz: full config backup
- tar -czf /tmp/etc.tgz /etc/config/: manual backup
- scp root@192.168.1.1:/etc/config/ /tmp/: remote copy

## Restore
- sysupgrade -r /tmp/backup.tar.gz: restore from backup
- tar -xzf /tmp/etc.tgz -C /: manual restore
- uci import < /tmp/config.txt: UCI import

## What to Backup
- /etc/config/: all configuration
- /etc/dropbear/: SSH keys
- /etc/opkg/: package lists
- /etc/crontabs/: cron jobs
- Custom scripts in /etc/init.d/
