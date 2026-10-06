"""List tools module for Practical Work 2."""


def sum_numbers(numbers: list[int | float]) -> int | float:
    """Return the sum of all items; 0 for an empty list."""
    total = 0
    for number in numbers:
        total += number
    return total


def max_number(numbers: list[int | float]) -> int | float:
    """Return the largest item; raise ValueError for an empty list."""
    if not numbers:
        raise ValueError("max_number() requires a non-empty list")
    result = numbers[0]
    for number in numbers:
        if number > result:
            result = number
    return result


def min_number(numbers: list[int | float]) -> int | float:
    """Return the smallest item; raise ValueError for an empty list."""
    if not numbers:
        raise ValueError("min_number() requires a non-empty list")
    result = numbers[0]
    for number in numbers:
        if number < result:
            result = number
    return result


def count_even(numbers: list[int | float]) -> int:
    """Return the number of even items; 0 for an empty list."""
    count = 0
    for number in numbers:
        if number % 2 == 0:
            count += 1
    return count


def reverse_numbers(numbers: list[int | float]) -> list[int | float]:
    """Return a new list with the items in reverse order."""
    return numbers[::-1]
