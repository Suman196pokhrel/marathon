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


