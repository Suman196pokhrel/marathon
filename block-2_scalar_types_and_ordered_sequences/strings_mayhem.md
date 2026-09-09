### Str
A string is an immutable sequence of characters. No operation modifies a string. Every "modification" allocates a new string and copies.
```python
s = "abc"
s.upper()        # returns "ABC"
print(s)         # "abc", unchanged
```

Every string method returns a new string. If you forget to assign the result, nothing happens. This is the most common beginner string bug.


# Concatenation in a loop
```python
s = ""
for c in chars:
    s+=c            # n iterations
```

s += c cannot mutate, so each step allocates a new string and copies everything accumulated so far. 
Iteration 1 copies 1 char, iteration 2 copies 2, and so on: 1+2+3+...+n, which is O(n²). (HOW ?)

```python
s = "".join(chars)   # O(n)
```
join walks the list once to compute the total length, allocates one buffer, then copies each piece in. One allocation, one pass.

Mental model: += is repeatedly rebuilding the whole wall to add a brick. join measures first, builds once.


--
### Why join is on the separator
```python
",".join(["a", "b"])     # "a,b"
```
Looks backwards, but join accepts any iterable of strings: list, tuple, set, generator, dict keys. If it were list.join(sep), every iterable type would need its own copy. 
Putting it on str gives one implementation for all of the


### Searching in strings
```python
"hello".find("z")      # -1
"hello".index("z")     # ValueError
"z" in "hello"         # False
```
Three ways, three failure styles. Use in for a yes/no question, find when you want a position and can handle absence, index when absence is a genuine error.


