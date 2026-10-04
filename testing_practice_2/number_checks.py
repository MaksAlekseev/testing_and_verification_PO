"""Проверки и простые операции над целыми числами.

Контракт функций приведён в docs/number_checks_contract.md.
"""


def is_even(n: int) -> bool:
    """Вернуть True, если целое число n чётное."""
    return n % 2 == 0


def is_positive(n: int) -> bool:
    """Вернуть True, если целое число n строго больше нуля."""
    return n > 0


def is_multiple(n: int, k: int) -> bool:
    """Проверить, делится ли n на k без остатка.

    Raises:
        ValueError: если k равен нулю.
    """
    if k == 0:
        raise ValueError("k не может быть равен нулю")
    return n % k == 0


def square(n: int) -> int:
    """Вернуть квадрат целого числа n."""
    return n * n


def last_digit(n: int) -> int:
    """Вернуть последнюю цифру абсолютного значения целого числа n."""
    return n % 10
