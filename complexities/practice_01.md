# Some basic questions to refresh Big O() estimation


# 1
```python
L = [1,2,3,4,5]

sum = 0
for i in L:                      # Loop1 ----> n
    sum = sum + i
print(sum)

product = 1                      # Loop2 ----> n
for i in L:
    product = product * i
print(product)
                                # Overall --> 2n --> n ---> Big O(n)
```


# 2
```python
L = [1,2,3,4,5]
for i in L:                             # Loop 1 -----> n
    for j in L:                         # For every i 2nd loop --->
        print("({}{})".format(i,j))   # total 2nd loop ops ---->  n * n -> Big O(n^2)
```


# 3
```python
Linear search algo => Big O(n)
```

# 4
```python
def intToStr(i):
    digits = '0123456789'
    if i == 0:
        return '0'
    result = ''
    while i > 0:                        # for every x10 in input size we get only
        result = digits[i%10] + result    # +1 increase in iteration => Big O(log n)
        i = i // 10
    return result
```


# 5
```python
n = 1000
i,j,k = 0

for(i= n/2; i < n; i++):        # Get executed n/2 times
    for(j = 2; j<=n;j=j*2):     # Get executed log n times
        k = k+n /2              # Overall n/2 * log n --> Big O (n.log n)

```


# 6
```python
Binary search    ----> Big O (log n)
```

# 7
```python
simple factorial ---> linear -> Big O (n)
```

# 8
```python
fibonacci using recursion --->  exponential --> Big O (2^n)
```

# 9
```python
mod operation with algebraic operations only -->> Constant --> Big O (1)
```
