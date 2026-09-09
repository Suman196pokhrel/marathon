# Hashes
A hash function turns a key into a number. That number tells you which slot to look in. So you jump straight there instead of searching.
That is the whole trick, and it is the reason dict and set lookup is O(1) while list lookup is O(n).

Finding "apple" later: hash it again, get slot 1, look there. One step. No scanning.

Contrast a list: to find "apple" you check element 0, then 1, then 2, until you find it. n steps.

The trade: you allocate a table bigger than the number of items (typically ~1/3 empty or more) and you pay a hash computation on every operation. Memory and a constant-time computation, in exchange for skipping the search. That is why a dict uses more memory than a list of the same items.

```python
"apple" --hash--> 8371625193 --% 8--> slot 1
                                       ↓
table:  [ ][apple][ ][ ][ ][ ][ ][ ]
```

### Hash is practice
```python
hash("apple")     # some large int
hash(42)          # 42, small ints hash to themselves
hash((1, 2))      # computed from the elements
hash([1, 2])      # TypeError: unhashable type: 'list'
```
Same value in, same number out, every time within one run.

The hash is not a label attached to a key you have to find. The hash is the location. You compute it from the key you are holding, in your hand, right now. You do not need to find "apple" in the dict, because you already have "apple" in your hand.

### Storage

A dict is an array of slots. On insert:
```python
d["apple"] = 5
hash("apple") → 8371625193
8371625193 % 8 → slot 1
Store the pair ("apple", 5) in slot 1
slot:  0      1               2   3   4   5   6   7
      [ ]  [("apple", 5)]    [ ] [ ] [ ] [ ] [ ] [ ]
```

### Lookup
```python
d["apple"]
hash("apple") → 8371625193 (same input, same output, always)
% 8 → slot 1
Jump directly to slot 1. Array indexing, O(1), like arr[1]
Read it
```


Zero keys were examined. Slots 0, 2, 3, 4, 5, 6, 7 were never touched. There was no scan.

### The analogy

A library where the shelf position is computed from the title.

List: walk the shelves from the start, reading every spine, until you find the book. n steps.
Dict: a rule says "this title goes on shelf 47." Apply the rule, walk to shelf 47. One step, whether the library has 100 books or 10 million.



### The contract

Two rules. Everything else in this section is a consequence.
- Rule 1: if a == b, then hash(a) == hash(b).
- Rule 2: an object's hash must never change during its lifetime.


### Collisions
Two different keys can hash to the same slot. Unavoidable: infinitely many possible keys, finitely many slots.
CPython uses probing: if the slot is taken by a different key, try another slot by a defined rule, repeat until an empty one is found. Lookup does the same walk, comparing keys along the way, until it finds the key or hits an empty slot (which proves absence).

This is why __eq__ still matters. The hash gets you to a slot. == confirms you found the right key. Both are used on every lookup:

Hash → slot
Compare keys with == (fast path: identity check first)
Mismatch → probe the next slot


### Is dict lookup always O(1)?

No. It is O(1) average, O(n) worst case.

The worst case is total collision: every key lands on the same slot, probing degenerates into a linear scan of n entries.
```python
class Bad:
    def __hash__(self): return 1      # every instance collides
    def __eq__(self, o): return self is o
```


### Why it is O(1) in practice:

Built-in hash functions distribute well
Python keeps the table sparse (it resizes when about two thirds full), so probes are short