# Kernel Config Issues

## Problem
After applying patches, `make silentoldconfig` fails with:
```
The present kernel configuration has modules disabled.
Type 'make config' and enable loadable module support.
Then build a kernel with module support enabled.
```

## Root Cause
OpenWrt's config fragments set CONFIG_MODULES=y, but the generated .config
doesn't include it because the base config wasn't loaded first.

## Fix
1. Start with defconfig: `make defconfig`
2. Apply kernel config fragment
3. Run silentoldconfig again

Or manually add to .config:
```
CONFIG_MODULES=y
CONFIG_MODULE_FORCE_LOAD=y
CONFIG_MODULE_UNLOAD=y
CONFIG_MODULE_FORCE_UNLOAD=y
```
