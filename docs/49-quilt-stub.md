# Quilt Stub Workaround

## Problem
OpenWrt's kernel build uses quilt to apply patches, but quilt is not installed
on modern Arch Linux by default.

## Solution
Created a minimal quilt stub:
```bash
#!/bin/bash
case "$1" in
  --quiltrc=*) shift ;;
esac
case "$1" in
  next) exit 1 ;;  # no more patches
  top) exit 0 ;;
  push) exit 0 ;;
  *) exit 0 ;;
esac
```

## Why This Works
OpenWrt checks `quilt next` to see if patches exist. If exit 1, it assumes
no patches and skips. Since we manually applied patches earlier, this is safe.

## Location
~/.local/bin/quilt
