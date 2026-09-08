# 1
a = [1, 2]
b = a
b = b + [3]
print(a, b)

# 2
a = [1, 2]
b = a
b += [3]
print(a, b)

# 3
x = 5
y = x
y += 1
print(x, y)

# 4
a = b = [0]
a += [1]
print(a, b)

# 5
t = ([1], 2)
t[0].append(9)
print(t)

# 6
# t = ([1], 2)
# t[0] += [9]
# print(t)          # careful, this one has two things happening

# 7
def f(d):
    d = {"new": 1}
d = {"old": 1}
f(d)
print(d)

# 8
a = [1, 2, 3]
b = a
a[:] = [9]
print(b)