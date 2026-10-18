# bison Patch Details

## Problem
bison-2.7's fseterr.c uses `_IO_ftrylockfile` which was removed in glibc 2.38.
The first `#if` branch fails to compile.

## Fix
Changed:
```c
#if defined _IO_ftrylockfile || __GNU_LIBRARY__ == 1
```
To:
```c
#if defined __GLIBC__ || defined _IO_ftrylockfile || __GNU_LIBRARY__ == 1
```

This ensures the GNU libc branch is taken, which uses `fp->_flags |= _IO_ERR_SEEN`
(still present in glibc 2.38's struct_FILE.h).

## File
build_dir/host/bison-2.7/lib/fseterr.c
