### int
int is arbitary precision, no overflow. Consequence : 32-bit overflow problems need explicit bounds check, python will not wrap.

### float
float is binary, so 0.1 + 0.2 != 0.3. Some decimals have no exact binary form like 1/3 in decimal. Compare with math.isclose

```text
## 1. Why `0.1 + 0.2 != 0.3`

In base 10, fractions like $1/3$ cannot be represented with a finite number of digits ($0.3333...$). Similarly, binary (base 2) cannot precisely represent fractions whose denominators have prime factors other than 2.

Because $0.1 = 1/10 = 1/(2 \times 5)$, its denominator contains a prime factor of 5. Therefore, $0.1$ and $0.2$ are infinite repeating fractions in binary:

$$\begin{aligned} 0.1_{10} &= 0.00011001100110011..._2 \\ 0.2_{10} &= 0.00110011001100110..._2 \end{aligned}$$

Python uses IEEE 754 double-precision floating-point numbers, which store numbers in 64 bits: **1 sign bit**, **11 exponent bits**, and **52 mantissa (fraction) bits** (yielding 53 bits of precision with the implicit leading 1).

Because the mantissa must fit in 53 bits, the repeating binary sequence is rounded to the nearest representable float:

* **Stored `0.1`**: `0.1000000000000000055511151231257827021181583404541015625`
* **Stored `0.2`**: `0.200000000000000011102230246251565404236316680908203125`
* **Stored `0.3`**: `0.299999999999999988897769753748434595763683319091796875`

When you add the stored floating-point representations of `0.1` and `0.2`, the result is:

$$\text{Stored } 0.1 + \text{Stored } 0.2 = 0.3000000000000000444089209850062616169452667236328125$$

Comparing `0.30000000000000004` to `0.29999999999999999` returns `False`.s
```

### bool
bool is a subset of int. True ==1 , sum([True, False, True]) == 2

- / float
- //floor
- % module = spits out the remainder
- -7 // 2 == -4 and -7 % 2 == 1.

####  Why `-7 % 2` is Positive in Python

Programming languages handle floor division and modulo for negative numbers in two main ways: **truncated division** (rounds toward zero) and **floored division** (rounds toward negative infinity). 

Python strictly follows **floored division** to preserve the fundamental division identity for all integers:

$$a = (a // b) \times b + (a \% b)$$

When evaluating `-7 // 2`:
* Floating-point division gives $-3.5$.
* Flooring $-3.5$ (rounding down toward $-\infty$) yields **$-4$**.

Plugging this into the division identity:

$$\begin{aligned} -7 &= (-7 // 2) \times 2 + (-7 \% 2) \\ -7 &= (-4) \times 2 + (-7 \% 2) \\ -7 &= -8 + (-7 \% 2) \\ -7 \% 2 &= 1 \end{aligned}$$

Because Python floors the quotient down to $-4$, the remainder must be **$+1$** to restore $-7$. 


A key mathematical property of Python's modulo operator is that **$a \% b$ always shares the sign of the divisor $b$**.



- Python floors, C truncates. Means -1 % n == n -1, so wraparound just works. 
- round is banker's rounding: round(0.5) == 0
- divmod, abs, pow(a, b, m), math.isqrt, math.gtd, float('inf')
- chained comparison a<b<c