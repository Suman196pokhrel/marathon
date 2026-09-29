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

## Stack

Notebooks: [stacks-using-arrays.ipynb](stacks-using-arrays.ipynb), [stacks.ipynb](stacks.ipynb) (linked list based)

Last in, first out (LIFO). You only ever touch the top, like a pile of plates.
Used for undo/redo, matching brackets, and function calls.

| Operation | Time |
| --- | --- |
| push | O(1) |
| pop | O(1) |
| peek | O(1) |
| is empty | O(1) |

- **Array based:** simple and cache friendly, but a fixed-size array can overflow.
  A Python `list` avoids that by growing.
- **Linked list based:** never overflows, pushing is just a new head node.
- **Bad at:** you only get the newest item. Serving items in arrival order needs something else.

That need for first come, first served leads to the queue.

## Queue

Notebooks: [queues-using-linkedlist.ipynb](queues-using-linkedlist.ipynb), [queues_using_2_Stacks.ipynb](queues_using_2_Stacks.ipynb)

First in, first out (FIFO). Add at the rear, remove from the front, like a line at
a counter. Used for task scheduling and BFS.

Why not just use a `list`? `list.pop(0)` shifts every remaining item, so it is O(n).

**Linked list with front and rear pointers**

| Operation | Time |
| --- | --- |
| enqueue (at rear) | O(1) |
| dequeue (from front) | O(1) |

**Two stacks**: push into stack 1, and pop from stack 2. When stack 2 is empty, move
everything from stack 1 into it, which flips the order.

| Operation | Time |
| --- | --- |
| enqueue | O(1) |
| dequeue | O(1) amortized, O(n) when a transfer happens |

- **Good at:** fair, in-order processing at O(1) per operation.
- **Bad at:** no fast lookup. Asking "is X in here?" is still O(n).
- In real code, use `collections.deque`, which is O(1) at both ends.

Every structure so far needs O(n) to find a value, which leads to the hash table.
