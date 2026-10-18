# m4 Patch Details (glibc 2.38)

## c-stack.c
Problem: glibc 2.38 changed SIGSTKSZ from constant to sysconf(_SC_SIGSTKSZ)
Fix: Changed `#elif HAVE_LIBSIGSEGV && SIGSTKSZ < 16384` to `#elif 0`
This forces the `#undef SIGSTKSZ` / `#define SIGSTKSZ 16384` path

## freadahead.c
Problem 1: `_IO_IN_BACKUP` flag removed from glibc 2.38
Fix: Changed `fp->_flags & _IO_IN_BACKUP ? ...` to `0 ? ...`

Problem 2: `_IO_ftrylockfile` macro removed
Fix: Added `defined __GLIBC__ ||` to the first branch

## Result
m4 1.4.16 builds successfully on glibc 2.38
