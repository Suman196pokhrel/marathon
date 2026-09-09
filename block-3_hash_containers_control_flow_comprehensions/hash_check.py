# 1
print(hash(1) == hash(1.0) == hash(True))
print({1: 'a', 1.0: 'b', True: 'c'})

# 2
k = [1, 2]
d = {tuple(k): "ok"}
k.append(3)
print(d)

# 3
# print(hash((1, 2)))
# print(hash((1, [2])))

# 4
# class P:
#     def __init__(self, x): self.x = x
#     def __eq__(self, o): return self.x == o.x
# print(P(1) == P(1))
# print({P(1)})

# # 5
class Q:
    def __init__(self, x): self.x = x
    def __eq__(self, o): return self.x == o.x
    def __hash__(self): return hash(self.x)
print(len({Q(1), Q(1), Q(2)}))

# 6
s = frozenset([1, 2])
print(hash(s) == hash(frozenset([2, 1])))
print({s: "works"})

# # 7
class Bad:
    def __hash__(self): return 1
    def __eq__(self, o): return self is o
d = {Bad(): i for i in range(1000)}
print(len(d))            # correct, but what is the lookup cost?