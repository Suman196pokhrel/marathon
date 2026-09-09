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

### Creating Dicts
```python
{'a': 1, 'b': 2}
dict(a=1, b=2)                    # keyword form, keys must be identifiers
dict([('a', 1), ('b', 2)])        # from pairs
dict(zip(keys, values))           # two parallel lists -> dict
dict.fromkeys(['a','b'], 0)       # {'a': 0, 'b': 0}
{**d1, **d2}                      # merge, d2 wins on conflicts
d1 | d2                           # same thing, 3.9+
```
fromkeys trap: the default value is one shared object.
```python
d = dict.fromkeys(['a','b'], [])
d['a'].append(1)
print(d)        # {'a': [1], 'b': [1]}   same list
```

### Access
```python
d['k']                  # KeyError if missing
d.get('k')              # None if missing
d.get('k', 0)           # 0 if missing
d.setdefault('k', [])   # returns existing, or inserts default and returns it
d.pop('k')              # remove and return, KeyError if missing
d.pop('k', None)        # with default, safe
d.popitem()             # remove and return the LAST pair (3.7+)
```
setdefault does two things at once: returns the current value if present, otherwise inserts your default and returns that. 
It is the one-liner for building lists inside a dict.

```python
d.setdefault(key, []).append(item)
```

