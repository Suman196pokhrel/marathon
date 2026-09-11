Dynamic Typing : names have no type, objects do. A name can be rebound to any type.

Strong typing : no silent coercion across unrelated types. "1" + 1 raises TypeError. Contrast javascript, which returns "11".

Exception : numeric tower coerces internally. 1 + 2.0 -> 3.0, True + 1 -> 2.
The numeric tower

Python defines a hierarchy where each level is a subset of the one above:

Complex  ⊃  Real  ⊃  Rational  ⊃  Integral
complex     float     Fraction     int

bool sits below int as a subclass. Formalised in numbers (ABCs), practically enforced by the types themselves.

Why coercion is allowed here but not for "1" + 1:

Because widening is lossless and unambiguous. Every int is a real number, so 1 + 2.0 has exactly one correct answer. There is no guessing. "1" + 1 has two defensible answers: "11" or 2. Python refuses rather than picking. That is the strong-typing rule: coerce only when the conversion is mathematically forced, never when it is a judgement call.

The direction matters. Coercion only goes up the tower, never down:
```python
1 + 2.0        # 3.0    int widened to float
2.0 + 1j       # (2+1j) float widened to complex
```
The mechanism: int.__add__(float) returns NotImplemented. Python then tries the reflected operation, float.__radd__(int), which knows how to widen. That fallback is what makes mixed arithmetic work without every type knowing every other type.

--


Duck typing : an object's usability depends on which dunders it implements, not its class. Python checks whether the method exists, not whether the class matches. Implement the right dunder and your object works anywhere that method is used.


--


type(x) is C : checks the exact type.
isinstance(x,C): accepts subclasses. Prefer isinstance, except when you specifically must reject subclasses (the bool/int case below).

