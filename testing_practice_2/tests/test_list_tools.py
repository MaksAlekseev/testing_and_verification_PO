import pytest

from list_tools import (
    count_even,
    max_number,
    min_number,
    reverse_numbers,
    sum_numbers,
)


def test_sum_numbers_returns_sum_for_mixed_numbers():
    assert sum_numbers([3, -2, 4.5]) == 5.5


def test_sum_numbers_returns_zero_for_empty_list():
    assert sum_numbers([]) == 0


def test_max_number_returns_largest_value():
    assert max_number([3, 7, 2]) == 7


def test_max_number_handles_list_with_only_negative_values():
    assert max_number([-5, -2, -9]) == -2


def test_max_number_handles_single_item():
    assert max_number([-4]) == -4


def test_max_number_raises_value_error_for_empty_list():
    with pytest.raises(ValueError):
        max_number([])


def test_min_number_returns_smallest_value():
    assert min_number([3, 7, 2]) == 2


def test_min_number_handles_list_with_only_negative_values():
    assert min_number([-5, -2, -9]) == -9


def test_min_number_handles_single_item():
    assert min_number([4]) == 4


def test_min_number_raises_value_error_for_empty_list():
    with pytest.raises(ValueError):
        min_number([])


def test_count_even_returns_zero_for_empty_list():
    assert count_even([]) == 0


def test_count_even_counts_zero_and_negative_even_values():
    assert count_even([0, -2, -3, 5, 8]) == 3


def test_count_even_returns_zero_when_there_are_no_even_values():
    assert count_even([-3, 1, 5]) == 0


def test_reverse_numbers_reverses_order_in_new_list():
    source = [1, -2, 3]
    result = reverse_numbers(source)

    assert result == [3, -2, 1]
    assert result is not source


def test_reverse_numbers_does_not_change_original_list():
    source = [1, 2, 3]
    reverse_numbers(source)

    assert source == [1, 2, 3]


def test_reverse_numbers_returns_empty_list_for_empty_input():
    source = []
    result = reverse_numbers(source)

    assert result == []
    assert result is not source


def test_reverse_numbers_handles_single_item():
    assert reverse_numbers([7]) == [7]


def test_sum_numbers_includes_repeated_items():
    assert sum_numbers([2, 2, -1]) == 3


def test_sum_numbers_does_not_change_original_list():
    source = [1, 2, 3]
    sum_numbers(source)

    assert source == [1, 2, 3]


def test_max_number_does_not_change_original_list():
    source = [-3, -1, -2]
    max_number(source)

    assert source == [-3, -1, -2]


def test_min_number_does_not_change_original_list():
    source = [3, 1, 2]
    min_number(source)

    assert source == [3, 1, 2]


def test_count_even_does_not_change_original_list():
    source = [0, -2, 3]
    count_even(source)

    assert source == [0, -2, 3]
