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


