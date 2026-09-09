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


### Range
A lazy sequence. It stores start, stop, and step. It computes values on demand and never builds a list.
```python
range(10**9)                  # instant, a few dozen bytes
list(range(10**9))            # would need ~8 GB
```
range(1000000) and range(3) use the same memory. That is the headline property.
But it is a sequence, not a generator. It supports everything a sequence does:
```python
r = range(0, 100, 5)
len(r)          # 20
r[3]            # 15, computed as start + 3*step
r[-1]           # 95
r[2:5]          # range(10, 25, 5)  -> slicing returns a range
95 in r         # True
```
in is O(1) for integers. It does arithmetic (is the value in bounds and on a step boundary), not a scan. Contrast a list, where in is O(n).