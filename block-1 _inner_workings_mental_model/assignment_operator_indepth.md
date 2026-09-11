# The Assignment Operator, In Depth

Two separate things exist in the Python data model:

- **Objects**: a block of memory with structure. Every object has a type pointer, a reference count, and a payload.
- **Names**: labels living in a namespace, which is literally a dictionary. A name is an entry in a lookup table whose value is the address of an object.

Both live in RAM. A rough visual:

```
HEAP
  0x7f2a...: [1, 2, 3]        # the object

NAMESPACE (dict)
  { "x": 0x7f2a... }          # the name, pointing at the object
```

The assignment operator connects these two entities. It never copies, and it never creates an object on the left-hand side.

So when `x = [1, 2, 3]` runs:

1. The right-hand side is evaluated, producing an object in memory.
2. The current namespace is looked up.
3. The mapping `"x" -> <that object>` is stored in it.

Step 3 is the whole of assignment. Nothing is written *into* `x`, because `x` is not a container, it's a key in a dict.

## The heap

**In general:** a large pool you request pieces of at runtime. You ask for *n* bytes, the allocator finds a free block and hands back its address. The block stays alive until something frees it, regardless of which function created it. Flexible, but slower, and something has to track what's still in use.

**In Python:** every object is on the heap. No exceptions. The integer `5`, a list, a string, a function object, a class, a module, a namespace dict, a frame, all heap. There's no such thing as a Python object on the stack.

This is forced by the language design: objects can outlive the function that created them (you can return a list), and any object can be referenced from anywhere. So none of them can have stack lifetime.

There's a name for the whole thing: the **private heap**. All Python objects and their data structures live in one heap managed exclusively by the interpreter. Your code has no direct access to it.

## Frames

When Python executes `def greet(): ...`, it builds an object on the heap holding the compiled bytecode, the default arguments, the closure cells, `__name__`, `__doc__`. Then it binds the name `greet` to it. This is an ordinary heap object, just like a list or a string; you can pass it around, store it in a dict, give it attributes. It lives on the heap for as long as something references it. *Calling* it does not create or destroy it.

When you actually call `greet()`, Python creates a **frame**: the workspace for that one invocation. It holds the local variable slots, the evaluation stack, the instruction pointer, and a link to the caller's frame.

So where do frames live? On the heap: frames are Python objects too.

## Where things actually sit in the process

| Region | What lives there |
| --- | --- |
| **The heap** | Every Python object: namespace dicts, function objects, frame objects. In CPython an object is a C struct (`PyObject`) with a refcount and a type pointer, allocated through Python's own allocator (`pymalloc`) sitting on top of `malloc`. |
| **The C stack** | The interpreter's own C function calls. Not where your Python objects go. |
| **Static / global memory** | Interned small integers, some interned strings, type objects. |

**Lesson 1:** a name is a reference to an object. The reference and the object are two different things. Assignment changes the reference. Method calls may change the object.

## Final note

`=` is the assignment operator. It evaluates the right-hand side to produce an object, then binds the left-hand target to a reference to that object. In CPython the reference is a pointer to the object's heap block. Assignment never copies the object.

"Binding" means different things depending on the target form:

- A bare name (`x = ...`) creates or rebinds an entry in the current scope.
- `a[i] = v`, `a[i:j] = v`, and `obj.attr = v` do **not** bind names at all; they call methods that mutate an existing object.
