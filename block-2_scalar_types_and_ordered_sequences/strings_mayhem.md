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


### Splitting strings
```python
"a b  c".split()         # ['a', 'b', 'c']   no arg: splits on ANY whitespace run
"a b  c".split(" ")      # ['a', 'b', '', 'c']  with arg: exact, keeps empties
"a,b,c".split(",", 1)    # ['a', 'b,c']  : hrere , is the separator and 1 is the max splits we want . so for 1 , we split the string once , creating 2 partitions
```

### Partitions
```python
"a=b=c".partition("=")   # ('a', '=', 'b=c')  always 3 parts, splits once
"line1\nline2".splitlines()
```
partition is useful when you want "before and after the first separator" without index arithmetic.


### Strip is a character set
```python
"hello".strip("ho")     # "ell"
```
strip does not remove the substring "ho". It removes any character in the set {h, o} from both ends, repeatedly, until it hits a character not in the set.
Walk it: h is in the set, remove. e is not, stop left side. From the right: o is in the set, remove. l is not, stop. Result "ell".
```python
"xxhello".lstrip("x")          # "hello"
"file.txt".strip(".txt")       # "file"   -> 'e' survives by luck, misleading
"test.txt".strip(".txt")       # "es"     -> ate into the name
```
strip() with no argument removes whitespace, which is the 95% case and always safe.

--

### Case and tests
#### Cases
```python
s.lower() / s.upper() / s.title() / s.capitalize()
```

#### Tests
Tests return bools andoperate on thw whole string
```python
"abc".isalpha()      # True
"ab c".isalpha()     # False, space is not alpha
"".isalpha()         # False, empty is always False
"123".isdigit()
"a1".isalnum()
" \t".isspace()
```



### Transforming and padding
```python
"a-b-c".replace("-", "+")        # all occurrences
"a-b-c".replace("-", "+", 1)     # first only
"7".zfill(3)                     # "007"
"7".rjust(3, "0")                # "007"
"ab".ljust(5, ".")               # "ab..."
"ab".center(6, "-")              # "--ab--"
```


### f-string and Format specs
```python
name, x = "Sam", 3.14159
f"{name} has {x:.2f}"      # "Sam has 3.14"
```
Format spec: {value:[fill][align][width][,][.precision][type]}
```python
f"{x:.2f}"        # 3.14        fixed decimals
f"{x:>10}"        # right align in width 10   (< left, ^ center)
f"{1234567:,}"    # 1,234,567   thousands separator
f"{255:b}"        # 11111111    binary   (o octal, x hex)
f"{0.256:.1%}"    # 25.6%
f"{x=}"           # x=3.14159   debugging, prints name and value
```
f"{x=}" is the fastest debug print you have. Use it instead of print("x is", x).


### ORD / CHR
```python
ord('a')     # 97, character to code point
chr(97)      # 'a', code point to character
```
Characters are numbers. ord() gives you the number.
```python
ord('a')  # 97
ord('b')  # 98
ord('c')  # 99
...
ord('z')  # 122
```
Contiguous means no gaps: 97, 98, 99, ... 122. Consecutive, in alphabetical order. That is a property of the ASCII/Unicode table, and it is what makes the trick work.

Where it can be used ?
```python
def is_anagram(a, b):
    if len(a) != len(b):
        return False
    counts = [0] * 26
    for c in a:
        counts[ord(c) - ord('a')] += 1
    for c in b:
        counts[ord(c) - ord('a')] -= 1
    return all(v == 0 for v in counts)
```
Count up for one word, count down for the other. If they are anagrams, everything cancels to zero. O(n) time, O(1) space.

Note the second loop decrements rather than building a second array. One array, two passes.

