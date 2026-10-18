# mkimage Patch Details (Not Fixed)

## Problem
tools/mkimage uses kernel-style type definitions that conflict with glibc 2.38.

Error:
```
asm_types.c:11:1: error: return type defaults to 'int' [-Wimplicit-int]
/usr/include/asm-generic/int-ll64.h:30:44: error: conflicting types for '__s64'
```

## Root Cause
mkimage expects kernel headers, but glibc defines __s64/__u64 differently.

## Would Need
1. Add -D__KERNEL__ to isolate from glibc types
2. Or patch asm_types.c to use uint64_t/int64_t from stdint.h
3. Or use system mkimage from u-boot-tools

## Workaround
System mkimage (u-boot-tools) works for most cases.
Symlink to staging_dir/host/bin/mkimage
