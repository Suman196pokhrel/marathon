# Rebinding vs Mutating

**Rebinding** is changing what the label references.

```python
a = [1, 2, 3]
b = a

a = [9, 9, 9]   # rebinding: a now labels a different object
```

Operations that rebind:
- `=`

**Mutating** is changing the contents of the object itself.

```python
b.append(33)  # mutating
```

Operations that mutate:
- `.append`
- `.extend`
- `.sort`
- `.add`
- `.update`
- `.clear`, and more

---

## Augmented assignment: the case that trips people up

```python
a = [1, 2]
b = a
a += [3]          # calls list.__iadd__, mutates in place
print(b)          # [1, 2, 3]

a = [1, 2]
b = a
a = a + [3]       # builds a NEW list, then rebinds
print(b)          # [1, 2]
```

---

## Function arguments are just binding

Passing an argument binds the parameter name to the same object the caller holds, nothing more.

```python
def f(lst):
    lst.append(1)     # mutates the caller's object

def g(lst):
    lst = lst + [1]   # rebinds the local name only
```

---

## `del`

`del x` removes the name from the namespace. It does not delete the object. The object goes away only when nothing references it; that's reference counting, covered in Block 9.
