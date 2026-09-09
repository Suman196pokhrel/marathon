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

