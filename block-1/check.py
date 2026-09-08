# a = [1, 2, 3]
# b = a
# a[:] = [9]
# print(a, b)

# c = [1, 2, 3]
# d = c
# c = [9]
# print(c, d)

# a = "hello"
# b = "hel" + "lo"
# s = "hel"
# c = s + "lo"
# print(a is b, a is c, a == c)

# def f(): return 1000
# def g(): return 1000
# x = 1000; y = 1000
# print(f() is g(), x is y)


# class C:
#     count = 0
#     def inc(self): self.count += 1
# a, b = C(), C()
# a.inc(); a.inc()
# print(a.count, b.count, C.count)

# class C:
#     items = []
# a, b = C(), C()
# a.items.append(1)
# a.items = [9]
# a.items.append(8)
# print(a.items, b.items, C.items, a.__dict__)