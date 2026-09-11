# The Copy Ladder

**Shallow copy:** new outer container, same references inside, one level deep.
**Deep copy:** new outer container, and recursively new copies of everything reachable, all the way down.

```python
b = a                # alias,   0 new objects
b = a[:]             # shallow, 1 new object (outer only)
b = list(a)          # shallow
b = a.copy()         # shallow
b = copy.copy(a)     # shallow
b = copy.deepcopy(a) # deep, new objects all the way down
```
