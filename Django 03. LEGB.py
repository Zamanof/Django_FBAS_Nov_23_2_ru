"""
Local
Enclosing
Global
Builtin
"""

from math import pi as PI

print(f"Built in PI = {PI}")


def foo():
    # global PI
    PI = 25
    print(f"Enclosing PI = {PI}")

    def bar():
        nonlocal PI
        PI = "Salam"
        print(f"Local PI = {PI}")

    bar()
    print(f"Enclosing PI = {PI}")


PI = 678
print(f"Global PI = {PI}")
foo()
print(f"Global PI = {PI}")
