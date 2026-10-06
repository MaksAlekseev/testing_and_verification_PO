import pytest

from number_checks import is_even, is_multiple, is_positive, last_digit, square


@pytest.mark.parametrize(
    ("number", "expected"),
    [(-4, True), (-3, False), (0, True), (7, False), (100, True)],
)
def test_is_even(number, expected):
    assert is_even(number) is expected


@pytest.mark.parametrize(
    ("number", "expected"),
    [(-1, False), (0, False), (1, True), (25, True)],
)
def test_is_positive(number, expected):
    assert is_positive(number) is expected


@pytest.mark.parametrize(
    ("number", "divisor", "expected"),
    [(0, 5, True), (12, 3, True), (-12, 3, True), (12, -5, False), (-12, -4, True)],
)
def test_is_multiple(number, divisor, expected):
    assert is_multiple(number, divisor) is expected


def test_is_multiple_raises_for_zero_divisor():
    with pytest.raises(ValueError):
        is_multiple(10, 0)


@pytest.mark.parametrize(("number", "expected"), [(0, 0), (3, 9), (-4, 16), (10**20, 10**40)])
def test_square(number, expected):
    assert square(number) == expected


@pytest.mark.parametrize(
    ("number", "expected"),
    [(0, 0), (7, 7), (120, 0), (-123, 3), (-120, 0)],
)
def test_last_digit(number, expected):
    assert last_digit(number) == expected
