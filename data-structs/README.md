# Data Structures

Core data structures built from scratch in Python. Each one fixes a weakness of the
one before it, so reading top to bottom tells a story: what it is good at, where it
hurts, and what came next to fix that.

`n` is the number of items stored.

## Static array

Notebook: [custom-array.ipynb](custom-array.ipynb) (the base array it grows on top of)

A fixed-size block of contiguous memory. Every slot sits right next to the last one,
so finding slot `i` is simple math: `start + i * slot_size`.

| Operation | Time |
| --- | --- |
| Read / write by index | O(1) |
| Search by value | O(n) |
| Insert / delete in the middle | O(n), everything after it shifts |

- **Good at:** instant index access, cache friendly, no extra memory per item.
- **Bad at:** the size is fixed when it is created. Once it is full, you cannot add more.

That fixed size leads to the dynamic array.

## Dynamic array

Notebooks: [custom-array.ipynb](custom-array.ipynb), [dynamic-array.ipynb](dynamic-array.ipynb)

A static array that grows itself. When it is full, it allocates a bigger block
(double the size in `custom-array.ipynb`), copies everything over, and carries on.
Python's `list` works this way, though CPython grows by a smaller factor than 2x.
`dynamic-array.ipynb` shows this with `sys.getsizeof` jumping in steps.

| Operation | Time |
| --- | --- |
| Read / write by index | O(1) |
| Append / pop at the end | O(1) amortized, O(n) on the append that triggers a resize |
| Search by value | O(n) |
| Insert / delete at the front or middle | O(n) |

- **Good at:** everything an array is good at, without having to pick a size up front.
- **Bad at:** inserting or deleting anywhere but the end still shifts items. Resizes copy
  every element, and spare capacity wastes memory.

The shifting cost at the front leads to the linked list.

## Singly linked list

Notebook: [single-linedlist.ipynb](single-linedlist.ipynb)

A chain of nodes. Each node holds a value and a pointer to the next node. Nodes live
anywhere in memory, so nothing ever needs to shift or be copied.

| Operation | Time |
| --- | --- |
| Insert / delete at the head | O(1) |
| Access by index | O(n), you walk from the head |
| Search by value | O(n) |
| Append at the tail | O(n) without a tail pointer, O(1) with one |
| Insert / delete after a known node | O(1) |

- **Good at:** cheap inserts and deletes at the front, grows one node at a time with no resizing.
- **Bad at:** no random access, an extra pointer per item, and poor cache locality.

Arrays and linked lists are general purpose. Often you only need to touch one end,
which leads to the stack.
