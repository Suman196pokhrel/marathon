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

