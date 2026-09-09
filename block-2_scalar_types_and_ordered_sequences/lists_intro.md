### Lists
A list is a contiguous array of references , with spare capacity at the end.

Two halves to that, and both matter:

Contiguous array → index access is O(1) (jump straight to slot i), but inserting or deleting anywhere except the end requires shifting everything after it.
Of references → the list holds pointers, not objects. That is why a list can mix types, and why [[0]*3]*3 breaks(here breaks means interms of mutability)

### Why append is O(1) but insert(0,x) is O(n)
append(d) drops it into the next free slot. One write, done. O(1).

insert(0, x) needs slot 0, which is occupied. Everything must shift right one place:
```python
[a][b][c] -> [ ][a][b][c]     3 moves
```

n items means n moves. Same for pop(0): everything shifts left to close the gap. The end is cheap, the front is expensive.
If you need both ends, collections.deque gives O(1) at both. The trade is that a deque has no O(1) middle indexing.


--

### Methods, and their costs
| Method | What it does | Cost |
| --- | --- | --- |
| `append(x)` | Add to end | $O(1)$ amortized |
| `extend(it)` | Add all items from an iterable | $O(k)$ |
| `insert(i, x)` | Insert before index `i` | $O(n)$ |
| `remove(x)` | Delete first item equal to `x`, raises `ValueError` | $O(n)$ |
| `pop()` | Remove and return last item | $O(1)$ |
| `pop(i)` | Remove and return item at index `i` | $O(n)$ |
| `index(x)` | Return first index of `x`, raises `ValueError` | $O(n)$ |
| `count(x)` | Count occurrences of `x` | $O(n)$ |
| `reverse()` | Reverse in place | $O(n)$ |
| `sort()` | Sort in place | $O(n \log n)$ |
| `copy()` | Shallow copy | $O(n)$ |
| `clear()` | Remove all items | $O(n)$ |
| `x in lst` | Membership test | $O(n)$ |

extend takes any iterable, so a.extend("ab") gives ['a', 'b']. Surprises people.


remove vs pop vs del is the trio people confuse:
```python
lst = ['a', 'b', 'c']
lst.remove('b')     # by VALUE, returns None
lst.pop(1)          # by INDEX, returns the item
del lst[1]          # by INDEX, returns nothing, also works on slices
```


### Key and reverse
Key is a function applied to each element; sorting happens on the results
```python
words = ["banana", "kiwi", "apple"]
sorted(words, key=len)              # ['kiwi', 'apple', 'banana']
sorted(words, key=str.lower)
sorted(nums, reverse=True)
```
key is called once per element (n calls), then sorting compares the computed values. So an expensive key function is fine.

