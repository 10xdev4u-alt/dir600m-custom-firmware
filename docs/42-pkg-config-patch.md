# pkg-config/glib Patch Details

## Problem
glib-1.2.10 uses `extern inline` which changed semantics in GCC 10+ (C99 inline rules).
The `G_INLINE_FUNC` macro in glib.h expands to `extern inline` under `__OPTIMIZE__`.
With modern GCC, `extern inline` means "provide external definition", causing
multiple definition errors at link time.

## Fix
Add `-std=gnu89` to HOST_CFLAGS in rules.mk:
```
HOST_CFLAGS:=-O2 -fcommon -std=gnu89 $(HOST_CPPFLAGS)
```

This restores the GNU89 inline semantics where `extern inline` means
"inline only, no external definition".

## Also
`-fcommon` needed for glib's `g_bit_storage` etc. which are defined in headers
without `extern` (tentative definitions merged by -fcommon).
