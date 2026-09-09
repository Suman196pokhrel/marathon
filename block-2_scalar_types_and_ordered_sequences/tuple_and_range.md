### Tuple
A tuple is an immutable sequence, and immutability buys you two things a list cannot have: hashability and safe sharing.
"safe sharing" refers to the ability to share a tuple across different functions, modules, or multithreaded workers without risking accidental data modifications or race conditions.

### Packaging
commas make a tuple. Parentheses are optional and usually just grouping.
```python
t = 1, 2, 3          # packing, no parens needed
a, b, c = t          # unpacking
```
Unpacking requires exact length, or it raises:
```python
a, b = (1, 2, 3)     # ValueError: too many values to unpack
```


### Swap
```python
a, b = b, a
```

Works because the right side is fully evaluated first into a tuple, then unpacked. So (b, a) is built from the old values before either name is rebound. No temp variable needed, no ordering hazard.


-- 



Starred unpacking absorbs the rest into a list (always a list, never a tuple):
```python
first, *rest = [1, 2, 3, 4]     # 1, [2, 3, 4]
*init, last = [1, 2, 3, 4]      # [1, 2, 3], 4
a, *mid, z = [1, 2, 3, 4]       # 1, [2, 3], 4
```


### Namedtuple
A tuple with named fields. Fixes the readability problem of p[2].
```python
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])

p = Point(1, 2)
p.x          # 1
p[0]         # 1, still a tuple
x, y = p     # still unpacks
```


