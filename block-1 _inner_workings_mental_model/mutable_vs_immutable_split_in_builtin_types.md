# Mutable vs Immutable: The Built-in Type Split

## Mutability

An object is **mutable** if its value can change after creation while its identity stays the same.

## Immutability

An object is **immutable** if no operation can change its value: anything that looks like a change instead produces a new object, with a new identity.

```python
a = [1, 2]
before = id(a)
a.append(3)
id(a) == before      # True, changed in place, mutable

s = "ab"
before = id(s)
s += "c"
id(s) == before      # False, new object, immutable
```

**Note:** mutability is a property of the *type*, not the variable. `x` is not mutable or immutable; the object `x` points at is.

---

## The split

**Immutable**

| Type | Notes |
| --- | --- |
| `int`, `float`, `complex`, `bool` | `bool` is a subclass of `int` |
| `str` | Every method returns a new string |
| `bytes` | The immutable byte sequence |
| `tuple` | Shallow immutability, see below |
| `frozenset` | Hashable version of `set` |
| `range` | A lazy sequence, fixed at creation |
| `NoneType`, `Ellipsis`, `NotImplemented` | Singletons |
| Type objects (mostly) | Built-in types cannot be modified |

**Mutable**

| Type | Notes |
| --- | --- |
| `list` | |
| `dict` | |
| `set` | |
| `bytearray` | The mutable counterpart to `bytes` |
| User-defined classes | Unless you deliberately prevent it |
| Most stdlib containers | `deque`, `defaultdict`, `Counter`, `OrderedDict` |
| Module objects, function objects | You can set attributes on them |

---

## The three consequences

Everything you need mutability for reduces to these:

1. **Aliasing.** Mutable objects can be changed through any reference. Immutable ones cannot, so sharing them is always safe. This is why `a = b = 0` is harmless and `a = b = []` is a bug waiting to happen.

2. **Hashability.** A hash must stay constant for an object's lifetime, otherwise it would go missing in its own dict. So mutable built-ins are unhashable by design.

   ```python
   {[1, 2]: "x"}        # TypeError: unhashable type: 'list'
   {(1, 2): "x"}        # fine
   {frozenset([1, 2])}  # fine
   ```

   Not the reverse, though; immutable does not guarantee hashable (see the note on sets below).

3. **Function arguments.** A function can mutate a mutable argument and the caller sees it. It can never affect the caller through an immutable one.

**Note:** a set itself is mutable, but the items inside a set must be immutable and hashable.

---

## Two traps worth memorising

### Mutable default arguments

Defaults are evaluated once, at `def` time, and the object persists across calls.

```python
def f(x, acc=[]):
    acc.append(x)
    return acc
f(1); f(2)           # [1, 2], not [2]
```

**What actually happens at `def`:** it's a statement that executes. When Python runs it:

1. Evaluates the default expressions right there, once.
2. Builds a function object.
3. Stores those evaluated defaults on the function object.
4. Binds the name.

So `acc=[]` runs `[]` a single time, at definition. The resulting list is attached to the function and lives as long as the function does.

`f.__defaults__` is the smoking gun. There is no "fresh default per call" mechanism; there's one object, sitting in the function object's heap block, from `def` until the function is garbage collected.

### Mutable class attributes

Shared by all instances, for the same reason: a `class` body executes once, at class-definition time (see [class_structure.md](class_structure.md)).

```python
class C:
    items = []       # one list, shared by the whole class
```
