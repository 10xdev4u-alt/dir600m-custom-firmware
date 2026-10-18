# mini_fo Filesystem

## Overview
mini_fo is a stackable filesystem that provides copy-on-write (CoW) functionality.
Used in OpenWrt for the overlay filesystem.

## How It Works
- Stacked on top of another filesystem (e.g., JFFS2)
- Intercepts write operations
- Creates copies of modified files
- Original filesystem remains read-only

## Benefits
- Read-only rootfs (SquashFS) + writable overlay (JFFS2)
- Config persists across reboots
- Factory reset = clear overlay

## Patches (2.6.30)
- 209-mini_fo.patch: base support
- 210-217: bug fixes for 2.6.25-2.6.30
- 999-use_preinit_as_init.patch: mount overlay at boot
