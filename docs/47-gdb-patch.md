# gdb Patch Details (Not Fixed)

## Problem
gdb-7.5 uses `wcwidth` which was removed from glibc's public headers in 2.38.

Error:
```
complete.c:687:19: error: implicit declaration of function 'wcwidth'
```

## Root Cause
glibc 2.38 moved wcwidth to <wchar.h> with _GNU_SOURCE, but gdb includes
<ctype.h> only.

## Would Need
1. Add #include <wchar.h> to complete.c
2. Or define _GNU_SOURCE at top of file
3. Or use system gdb (already on host)

## Workaround
GDB not needed for firmware build. Skip it:
- Remove CONFIG_GDB=y from .config
- Or create stub toolchain/gdb/Makefile
