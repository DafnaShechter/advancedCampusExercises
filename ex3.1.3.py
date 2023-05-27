def throw_stop_iteration():
    raise StopIteration("StopIteration exception occurred")

def throw_zero_division():
    raise ZeroDivisionError("ZeroDivisionError exception occurred")

def throw_assertion_error():
    raise AssertionError("AssertionError exception occurred")

def throw_import_error():
    raise ImportError("ImportError exception occurred")

def throw_key_error():
    raise KeyError("KeyError exception occurred")

def throw_syntax_error():
    raise SyntaxError("SyntaxError exception occurred")

def throw_indentation_error():
    raise IndentationError("IndentationError exception occurred")

def throw_type_error():
    raise TypeError("TypeError exception occurred")


# Call each function and handle the exceptions
try:
    throw_stop_iteration()
except StopIteration as e:
    print(str(e))

try:
    throw_zero_division()
except ZeroDivisionError as e:
    print(str(e))

try:
    throw_assertion_error()
except AssertionError as e:
    print(str(e))

try:
    throw_import_error()
except ImportError as e:
    print(str(e))

try:
    throw_key_error()
except KeyError as e:
    print(str(e))

try:
    throw_syntax_error()
except SyntaxError as e:
    print(str(e))

try:
    throw_indentation_error()
except IndentationError as e:
    print(str(e))

try:
    throw_type_error()
except TypeError as e:
    print(str(e))
