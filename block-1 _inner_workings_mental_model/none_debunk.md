# `None`, Debunked

## What `None` is
- The sole instance of `NoneType`, a true singleton. `type(None)() is None` → `True`
- A keyword since Python 3, so it cannot be rebound or subclassed
- Falsy, no length, no iteration, no arithmetic

## What it means
- Absence of a value, not zero, not empty, not `False`
- Three uses: function returned nothing, argument not supplied, field genuinely empty

## Why `is None` over `== None`
- `==` is overridable, `is` is not. A class can define `__eq__` to return `True` against anything
- NumPy arrays return an array from `== None`, so `if arr == None` raises `ValueError`. `is None` works
- `is` is a pointer comparison, faster, with a dedicated bytecode fast path
- PEP 8 requires it; every linter flags `== None`

## Why not `if not x:`
- Falsy also catches `[]`, `""`, `0`, `0.0`, `{}`, `set()`, `False`
- So a caller passing an empty list silently gets the default instead
- `is None` distinguishes "not supplied" from "supplied as empty": different states, a real bug class
- Same trap with `str.find` returning index `0`, and with `d.get()` where a missing key and a `None` value look identical

## Sentinel pattern
- When `None` is a valid value the caller might pass, make your own: `_MISSING = object()`
- Compare with `is`. Its only property is unique identity

## `None` as a return value
- Every function without `return` returns `None`
- Mutating methods return `None` by convention: `list.sort()`, `.append()`, `dict.update()`
- `sorted(x)` returns new, `x.sort()` returns `None`. The asymmetry is deliberate signalling
- `x = x.sort()` is the classic bug
- `AttributeError: 'NoneType' object has no attribute X` almost always means something returned `None` and you assumed it returned an object

## Type hints
- `Optional[int]` means `int | None`, not "optional argument"
- Prefer `int | None` on 3.10+

## The rules
- `is None` / `is not None` when you mean absent
- `not x` only when you genuinely mean falsy, and you've decided `0` and `[]` belong in that branch
