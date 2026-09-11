# `id()`, and `is` vs `==`

## `id()`

Returns the identity of an object: unique among objects alive at the same time, constant for that object's whole life.

In CPython the implementation is the memory address. That's not guaranteed by the language, but as a mental hook: `id(x)` tells you which heap block `x` points to.

**One trap:** identities are only unique among *living* objects. Once an object is freed, its address can be reused.

```python
print(id([1, 2, 3]))
print(id([4, 5, 6]))   # can print the same number as above
```

## `is` vs `==`

- `==` asks: are the **values** the same?
- `is` asks: are they the **same object**? Equivalent to `id(x) == id(y)`, a pointer comparison. Always O(1), and cannot be overridden.
