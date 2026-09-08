# 1
a = 256; b = 256
c = 257; d = 257
print(a is b, c is d)

# 2
x = 1000
print(x is 1000)

# 3
print(int("256") is 256, int("257") is 257)

# 4
a = "hello"; b = "hel" + "lo"
print(a is b)

# 5
s = "hel"
a = "hello"; b = s + "lo"
print(a is b)

# 6
a = "hi there"; b = "hi there"
print(a is b)            # and is this interning or dedup?

# 7
print(1.0 is 1.0, () is (), [] is [], "" is "")

# 8
def f():
    a = 500
    b = 500
    return a is b
a = 500
b = 500
print(f(), a is b)       # explain any difference

# 9
print(True is 1, True == 1, bool is int)