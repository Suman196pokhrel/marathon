### Dictionary
A dict is the hash table from 3.1 with values attached. A set is the same table with no values. Everything about hashability, O(1) average lookup, and collisions carries over unchanged.


### Insertion order is maintained in dictionaries
Ordered means insertion-ordered, not sorted. People conflate these.
Reassigning a value does not move the key. The key keeps its original position. Deleting and reinserting does move it to the end.
```python
d = {'a': 1, 'b': 2}
d['a'] = 99      # still first
del d['a']; d['a'] = 99   # now last
```

