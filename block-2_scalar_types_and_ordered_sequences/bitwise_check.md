### The six Bitwise operator

| Operator | Name        | What it does                                               |
| -------- | ----------- | ---------------------------------------------------------- |
| `&`      | AND         | Produces `1` where **both bits are `1`**                   |
| `\|`     | OR          | Produces `1` where **at least one bit is `1`**             |
| `^`      | XOR         | Produces `1` where **the bits are different**              |
| `~`      | NOT         | **Flips** every bit: `0` becomes `1`, and `1` becomes `0`  |
| `<<`     | Left shift  | Moves the bits **left**, adding zeros on the right         |
| `>>`     | Right shift | Moves the bits **right**, dropping bits from the right end |



#### AND
```python
a =12 #1100
b = 10 #1010
```
A result bit is 1 only when both corresping bits are 1
 a & b = 1000 = 8 (Decimal system)


### Useful for checking whether particular bits are set:
```python
x = 13  # 1101

x & 1   # 1 → odd
```
The last bit represents 1. Every other position represents an even number, so:
```python
is_odd = (x & 1) == 1
```

### To check position K, counting from zero on the right:
```python
is_set = (x & (1 << k)) != 0
```

### Shifts: move the bits
Using 5, whose binary representation is 0101:
```python
5 << 1   # 0101 → 1010 → 10
5 >> 1   # 0101 → 0010 → 2
```
The 1 means move by one position.

For positive numbers, shifting left by one doubles the value; shifting right by one halves it, discarding any remainder.s