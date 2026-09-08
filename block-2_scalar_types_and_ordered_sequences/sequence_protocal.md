# Sequence protocal
A sequence is an ordered collection of items. Because items ahve , positions you can access the first item, second item and so on. The sequence protocol means they support a common set of operations.

Following are the python sequences
```python
"hello"          # str: characters
[10, 20, 30]     # list: items
(10, 20, 30)     # tuple: items
range(5)        # range: integers 0 through 4
b"hello"        # bytes: integers representing bytes
```


### Common operations
+, *, in, len, min, max, index, count, iteration, slicing

slicing syntax : sequence[start:stop:step]
- start: where to begin, included.
- stop: where to stop, excluded.
- step: how far to move between selections; defaults to 1.


a protocol describes expected behavior; dunder methods provide that behavior. You don’t need every operation from the earlier table to create a sequence.