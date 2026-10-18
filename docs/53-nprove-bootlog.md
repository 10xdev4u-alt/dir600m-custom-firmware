# nprove Boot Log (UART)

## Boot Sequence
```
---RealTek(RTL8196C)at 2010.08.19-10:51+0800 version v1.1c [16bit](390MHz)
sys checksum error at 00010000!
no sys signature at 00020000!
Jump to image start=0x80500000...
OpenWrt kernel loader for Realtek rtl819xx
Copyright (C) 2011 Gabor Juhos
Copyright (C) 2013 Roman Yeryomin
Decompressing kernel to 80000000... done!
Starting kernel from 80003530...
```

## Kernel Boot
```
[    0.000000] Dentry cache hash table entries: 4096
[    0.010000] Inode-cache hash table entries: 2048
[    2.040000] squashfs: version 4.0 (2009/01/31)
[    2.050000] Registering mini_fo version $Id$
[    2.060000] JFFS2 version 2.2
[   43.950000] <=== Load_92C_Firmware
[   43.950000] 0x55d = 0xff
```

## Notes
- WiFi firmware loads at 43.95s (slow)
- SquashFS mounts as root
- JFFS2 for overlay (rootfs_data)
