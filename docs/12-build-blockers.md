# Build Blockers Summary

## Host Tool Issues (glibc 2.38)
1. m4: SIGSTKSZ, freadahead -> PATCHED
2. pkg-config/glib: inline semantics -> PATCHED (-std=gnu89)
3. bison: fseterr -> PATCHED
4. mklibs: C++ throw specs -> PATCHED
5. cmake: C++17 dynamic exception specs -> NOT FIXED
6. e2fsprogs: __s64 type conflict -> NOT FIXED
7. gdb: wcwidth implicit decl -> NOT FIXED
8. mkimage: asm_types.c -> NOT FIXED

## Kernel Issues
- quilt patches not applying cleanly (stub used)
- CONFIG_MODULES not set in generated .config
- Need real quilt or manual patch application

## Verdict
Use old VM (Ubuntu 12.04/14.04) for reliable build.
