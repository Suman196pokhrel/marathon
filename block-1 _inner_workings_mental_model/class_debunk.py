import dis

code = compile("class C:\n    x = 1\n    def m(self): pass", "<s>", "exec")
dis.dis(code)

# OUTPUT
# spDev 💡.../DevStuff/projects/dsa-marathon                                                                                                                 
# ❯ python block-1/class_debunk.py
#   0           0 RESUME                   0

#   1           2 PUSH_NULL
#               4 LOAD_BUILD_CLASS
#               6 LOAD_CONST               0 (<code object C at 0x7f2ac0d6d070, file "<s>", line 1>)
#               8 MAKE_FUNCTION            0
#              10 LOAD_CONST               1 ('C')
#              12 PRECALL                  2
#              16 CALL                     2
#              26 STORE_NAME               0 (C)
#              28 LOAD_CONST               2 (None)
#              30 RETURN_VALUE

# Disassembly of <code object C at 0x7f2ac0d6d070, file "<s>", line 1>:
#   1           0 RESUME                   0
#               2 LOAD_NAME                0 (__name__)
#               4 STORE_NAME               1 (__module__)
#               6 LOAD_CONST               0 ('C')
#               8 STORE_NAME               2 (__qualname__)

#   2          10 LOAD_CONST               1 (1)
#              12 STORE_NAME               3 (x)

#   3          14 LOAD_CONST               2 (<code object m at 0x7f2ac11350b0, file "<s>", line 3>)
#              16 MAKE_FUNCTION            0
#              18 STORE_NAME               4 (m)
#              20 LOAD_CONST               3 (None)
#              22 RETURN_VALUE

# Disassembly of <code object m at 0x7f2ac11350b0, file "<s>", line 3>:
#   3           0 RESUME                   0
#               2 LOAD_CONST               0 (None)
#               4 RETURN_VALUE


# Read it as a stack machine:

# PUSH_NULL is calling-convention padding in 3.11. Every call expects a slot before the callable (for a bound self); there is none here, so NULL.
# LOAD_BUILD_CLASS pushes the builtin __build_class__. That is the function that actually does class creation. You can call it yourself: it is in builtins.
# LOAD_CONST 0 pushes the already-compiled code object for the class body. The compiler built it during compilation and stored it as a constant of the module.
# MAKE_FUNCTION 0 wraps that code object into a real function object. The class body is genuinely a function.
# LOAD_CONST 1 ('C') pushes the name.
# CALL 2 calls __build_class__(body_function, 'C').
# STORE_NAME 0 (C) binds the result.

# So the source-level statement class C: compiles down to a function call. That is the whole of phase 1 in one line:




