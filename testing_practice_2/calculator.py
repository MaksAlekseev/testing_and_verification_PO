"""Simple calculator module for Practical Work 2.

The module intentionally contains one seeded defect for the peer-testing
exercise. The tester should discover it from the agreed contract and tests.
"""


def add(a, b):
    return a + b

def subtract(a: int | float, b: int | float) -> int | float:
    """Return the difference a - b."""
    return a - b


def multiply(a: int | float, b: int | float) -> int | float:
    """Return the product of two numbers."""
    return a * b


def divide(a: int | float, b: int | float) -> float:
    """Return a divided by b; raise ZeroDivisionError when b is zero."""
    return a / b


def absolute_value(number: int | float) -> int | float:
    """Return the non-negative magnitude of a number."""
    return abs(number)
