### int
In C, an int is a fixed 32 or 64 bits of memory. The hardware adds two registers; if the result needs a 65th bit, that bit has nowhere to go and is discarded. That is overflow. It is a consequence of fixed-width storage.

Python does not use a machine register. A Python int is a heap object with a variable-length array inside it:
```c
struct {
    PyObject_HEAD       // refcount, type pointer
    ssize_t ob_size;    // number of digits, sign encoded here
    uint32_t ob_digit[]; // the digits themselves
};
```
Need more range? Allocate more digits. There is no fixed width to overflow, so overflow cannot happen. The ceiling is your RAM.

