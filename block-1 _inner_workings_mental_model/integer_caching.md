# Small Integer Caching & Interning

## Small integer caching

CPython pre-allocates integer objects from -5 to 256 inclusive at startup. Every expression producing a value in that range returns a reference to the existing object.

```python
a = 256
b = 256
print(a is b)        # True

a = 257
b = 257
print(a is b)        # depends, see below
```

Floats are not cached at all: `1.0 is 1.0` at runtime is `False`.

---

## The second mechanism people confuse with caching

When `a = 257; b = 257` gives `True`, that's usually *not* the small-int cache; it's the compiler.

Two separate compile-time behaviours:

1. **Constant folding.** The compiler evaluates constant expressions at compile time. `"py" + "thon"` becomes the single constant `"python"` before your program runs; no runtime concatenation occurs.

2. **Constant deduplication.** Within one code object, equal constants of the same type are stored once in `co_consts`.

```python
def f():
    a = 1000
    b = 1000
    return a is b
print(f())        # True, both LOAD_CONST point at the same entry
```

Both `1000` literals became one constant. This is why behaviour differs between a script and an interactive REPL: in a script the two lines compile into one code object; in the REPL each statement compiles separately, so each gets its own constant.

That version-and-context dependence is the entire reason using `is` to compare values is unreliable. It isn't one rule you can memorise; it's three interacting mechanisms.

---

## String interning

Interning means keeping a global table of strings so that equal strings share one object. It's automatic, at compile time, for string constants that look like identifiers: letters, digits, and underscores only, not starting with a digit.

```python
a = "hello"
b = "hello"
print(a is b)              # True, interned

a = "hello world"          # space, not identifier-like
b = "hello world"
print(a is b)              # True in one code object, via dedup, not interning
```

Also cached: the empty string, and all single-character latin-1 strings.

```python
print("" is "")                              # True
print(chr(97) is "a")                        # True
print(chr(300) is chr(300))                  # False, outside the cache
```

**Explicit interning:**

```python
import sys
a = sys.intern("hello world")
b = sys.intern("hello world")
print(a is b)              # True
```

---

## Summary

CPython preallocates integers from -5 to 256 and interns identifier-like string literals, so `is` can return `True` for values you didn't expect to share. Separately, the compiler folds constant expressions and deduplicates equal constants within a code object, which produces sharing even outside the cached ranges. All of it is implementation detail that varies by version and by whether the code compiles as one unit; `is` should only be used for singletons like `None`.

| Mechanism | What it does | Applies to | When it happens | Survives separate code objects? | Notes |
|---|---|---|---|---|---|
| **Small integer caching** | Reuses preallocated `int` objects | `int` in range **-5 to 256** | Runtime, any way the value is produced | **Yes** | Also called "integer interning" informally. `int("100") is 100` → `True` |
| **String interning** | Global table so equal strings share one object | `str` literals that look like **identifiers** (letters, digits, `_`, not starting with a digit). Also all identifiers, attribute names, function/class names | Compile time (automatic) or runtime via `sys.intern()` | **Yes** | `"hello"` interned, `"hi there"` not |
| **Singletons and small caches** | Exactly one object exists, forever | `None`, `True`, `False`, `()`, `""`, single-char latin-1 strings, `Ellipsis`, `NotImplemented` | Interpreter startup | **Yes** | `chr(97) is "a"` → `True` |
| **Constant folding** | Compiler evaluates constant expressions ahead of time | Any constant expression: `2+3`, `"py"+"thon"`, `(1,2)` | Compile time | n/a, it removes the computation | `"py"+"thon"` becomes one constant. `s+"lo"` does not, `s` is a name |
| **Constant deduplication** | Equal constants of the same type stored once in `co_consts` | Any constant: int, float, str, tuple, bytes | Compile time | **No** | The unreliable one. `1000 is 1000` → `True` in a script, `False` across functions |
