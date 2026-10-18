# e2fsprogs Patch Details (Not Fixed)

## Problem
e2fsprogs-1.42.7 includes <asm-generic/int-ll64.h> which conflicts with
glibc 2.38's definition of __s64/__u64.

Error:
```
/usr/include/asm-generic/int-ll64.h:30:44: error: conflicting types for '__s64';
have 'long long int'
```

## Root Cause
e2fsprogs expects kernel headers, but glibc now defines these types.

## Would Need
1. Patch asm_types.c to use __kernel_s64/__kernel_u64 instead
2. Or add -D__KERNEL__ to isolate from glibc types
3. Or use system e2fsprogs (already installed on host)

## Workaround
Use system e2fsprogs:
- e2fsck, mkfs.ext2/3/4 already on host
- Symlink to staging_dir/host/bin/
