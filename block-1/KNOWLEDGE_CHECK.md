A1. What does = actually do, step by step? What does it never do?

A2. Define rebinding and mutating. What single question tells you which one an operation is?

A3. Why is "is Python pass by value or pass by reference" a badly framed question? What is the correct answer?

A4. Where do Python objects live? What is on the OS stack, then?

A5. A function object and a frame object are two different things. What is each, when is each created, and how many of each exist for a function called 5 times recursively?

A6. What question does is ask? What question does == ask? What is the cost of each, and which one can a class override?

A7. Give a case where two objects are equal but not identical. Now give one where they are identical but not equal.

A8. Define immutable precisely. Does it mean the object's contents can never change? Justify with a tuple.

A9. Why can a tuple be a dict key but a list cannot? Is every tuple usable as a key?

A10. a += [3] on a list and s += "c" on a string look identical but behave differently. Explain the mechanism, not just the outcome.

A11. Explain the mutable default argument trap at the level of when the object is created and where it is stored. Why does acc=0 not have the same problem?

A12. For a class attribute, why does a.items.append(1) affect other instances but a.items = [9] does not? Answer in terms of the lookup algorithm.

A13. What exactly does a shallow copy duplicate, and what does it not? When is a shallow copy indistinguishable from a deep copy?

A14. Name two things deepcopy does beyond recursively copying.

A15. Name the caching and compile-time mechanisms that can make is return True unexpectedly. Which ones survive being split across two separate functions?

A16. Why x is None rather than x == None? And why is if not x: a different question rather than a shorter version of the same one?

A17. [] is [] is always False, in every version of Python. Explain why this is a correctness requirement, not a missing optimisation.

A18. In a backtracking problem, why must you write result.append(path[:]) instead of result.append(path)?



ANSWERS
Part A

A1. Evaluates the RHS to produce an object, then binds the LHS target to a reference to that object. In CPython the reference is a pointer to the object's heap block. It never copies the object, and it never creates anything on the left side. Caveat: only a bare name binds. a[0] = v, a[i:j] = v, and obj.attr = v bind no name; they call __setitem__ / __setattr__ and mutate an existing object.

A2. Rebinding changes which object a name points to. Mutating changes the object itself. The question: does the identity the name points to change, or does the object at that identity change? Rebinding is invisible to every other name. Mutation is visible to every name pointing at that object. Only = on a bare name rebinds; in-place methods, item assignment, slice assignment, and del a[i] mutate.

A3. Because it presupposes those are the only two options, and Python does neither. Arguments are passed by object reference: the parameter name is bound to the same object the caller holds. Whether the caller sees a change depends entirely on whether the object is mutable and whether the function mutates rather than rebinds.

A4. Every Python object is on the heap, specifically CPython's private heap managed by pymalloc. No exceptions: ints, strings, lists, functions, classes, modules, frames. The OS stack holds only the interpreter's own C function calls. Frames are used in stack order but are heap-allocated objects, which is why a generator's frame can survive after the function stops running.

A5. The function object is created once, when the def statement executes; it holds the code object, defaults, closure cells, __name__. The frame object is created per call and holds locals, the evaluation stack, and the instruction pointer. Five recursive calls: 1 function object, 5 frames.

A6. is asks "same object?", equivalent to id(x) == id(y). Pointer comparison, O(1), cannot be overridden. == asks "equal value?", calls __eq__, cost depends on type (O(n) for long lists), and any class can override it.

A7. Equal not identical: [1,2] == [1,2] is True, is is False. Identical not equal: n = float('nan'); n is n is True, n == n is False, because IEEE 754 says NaN equals nothing.

A8. Immutable means no operation can change the object's value while preserving its identity; anything that looks like a change produces a new object. It does not mean the contents can never change. t = ([1], 2): t[0].append(9) works, because the tuple's slots (the references) are fixed but the objects they point at may be mutable. Tuple immutability is shallow.

A9. A hash must stay constant for the object's lifetime, otherwise the object would go missing in its own dict. Mutable built-ins are therefore unhashable by design. Not every tuple works: a tuple is hashable only if everything inside it is. hash((1, [2])) raises TypeError.

A10. += asks the object whether it can mutate itself, via __iadd__. list.__iadd__ exists, so it extends in place and every alias sees it. str has no in-place option, so s += "c" builds a new string and rebinds the name, leaving aliases untouched. Consequence: string += in a loop is O(n²), which is why join exists.

A11. Default expressions are evaluated once, when the def statement executes, and the resulting objects are stored on the function object (visible as f.__defaults__). There is no per-call refresh. A mutable default is therefore one shared object for the function's whole life, and acc.append(x) mutates it permanently. With acc=0, the default is also shared, but acc += x cannot mutate an int, so it rebinds the local name and the stored default is never touched. Fix: None sentinel, construct in the body.

A12. Reading walks the MRO: check a.__dict__ (empty), fall through to C.__dict__, return the class's list. Every instance without its own entry lands on that same object, so mutating it is visible to all. Writing never walks the MRO: a.items = [9] goes straight into a.__dict__, creating an entry that shadows the class attribute for a only. b.__dict__ is still empty, so b still falls through. Reads walk up, writes stay on the instance.

A13. It duplicates only the outer container. The new container holds the same references as the original, so the contained objects are shared. It is indistinguishable from a deep copy when every contained object is immutable, because sharing an immutable object is unobservable. Rebinding a slot in the copy is safe; mutating what a slot points at is not.

A14. (1) It maintains a memo dict keyed by id(), which lets it terminate on reference cycles and preserves shared references as shared rather than duplicating them. (2) It returns immutable atomic objects as-is (ints, strings, functions, classes, modules) rather than copying them.

A15. Small integer caching (-5 to 256), string interning (identifier-like literals, plus sys.intern), singletons and small caches (None, True, False, (), "", single-char latin-1 strings), constant folding, and constant deduplication. The first three are runtime mechanisms and survive being split across functions. Folding and dedup are compile-time and scoped to one code object, so they do not.

A16. == can be overridden by any class, and some real types return non-booleans from it (a NumPy array returns an element-wise array, making if arr == None raise ValueError). is is a pointer comparison against a keyword-protected singleton, so it is exactly correct, cannot be fooled, and is faster. if not x: is a different question because falsy also covers [], "", 0, 0.0, {}, set(), False. It conflates "not supplied" with "supplied as empty", which silently overrides a caller who deliberately passed an empty container.

A17. If [] returned a shared object, then a = [] and b = [] would alias, and a.append(1) would change b. Every caching mechanism in Python applies only to immutable objects, because immutability is precisely what makes sharing unobservable. Sharing a mutable object would make aliasing universal and unavoidable.

A18. path is one mutable list being appended to and popped from throughout the recursion. result.append(path) stores a reference to that live list, so every entry in result is the same object and reflects whatever state it ends in (usually empty). path[:] takes a shallow snapshot, which is a genuinely separate list. It is the aliasing bug in its most common DSA form.ss