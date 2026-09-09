### Sets
A dict with only keys. Unordered, unique, elements must be hashable. Same O(1) average membership.

### Creating
```python
{1, 2, 3}
set([1, 2, 2, 3])     # {1, 2, 3}, dedups
set()                 # empty set
{}                    # EMPTY DICT, not a set
```

{} was taken by dicts first, so empty sets need set().

### Methods
```python
s.add(x)              # one element
s.update([1,2])       # many
s.remove(x)           # KeyError if missing
s.discard(x)          # silent if missing
s.pop()               # removes an ARBITRARY element
s.clear()

```
remove vs discard is the pair to remember. Use discard when absence is fine.

### Set algebra
```python
a | b     a.union(b)                  # in either
a & b     a.intersection(b)           # in both
a - b     a.difference(b)             # in a only
a ^ b     a.symmetric_difference(b)   # in exactly one

a <= b    a.issubset(b)
a < b     # proper subset
a.isdisjoint(b)                       # no common elements
```

Operators require both sides to be sets. Method forms accept any iterable.
```python
{1,2} | [3]              # TypeError
{1,2}.union([3])         # {1, 2, 3}
```

### frozenset
Immutable, therefore hashable, therefore usable as a dict key or an element of another set.
```python
fs = frozenset([1, 2])
{fs: "ok"}                    # works
{frozenset([1,2]), frozenset([2,1])}    # one element, order-insensitive
```

### When a set is right, and when it is wrong

Right:

- Deduplication: list(set(items))
- Membership testing in a loop
- Seen-tracking in BFS/DFS
- "Have I already processed this?"

Wrong:

- You need order (a set has none; list(set(x)) scrambles it)
- You need duplicates (use Counter)
- Elements are unhashable (lists, dicts)


### The interview points
Complexity of in:

| Type | Time Complexity | Notes / Details |
| --- | --- | --- |
| `list`, `tuple` | $O(n)$ | Linear search through elements |
| `set`, `dict` (keys) | $O(1)$ avg | Average $O(1)$ lookup via hashing ($O(n)$ worst-case) |
| `str` (substring) | $O(n \cdot m)$ | $n$ is string length, $m$ is substring length |
| `d.values()` | $O(n)$ | Must iterate over all values |