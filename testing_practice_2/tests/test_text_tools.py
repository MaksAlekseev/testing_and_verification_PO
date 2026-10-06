"""Tests for text_tools.py (author: Vitya, tester: Artem)."""

import pytest

from text_tools import (
    count_vowels,
    count_words,
    is_palindrome,
    remove_spaces,
    reverse_text,
)


# ---------- reverse_text ----------

def test_reverse_text_reverses_regular_word():
    assert reverse_text("abc") == "cba"


def test_reverse_text_returns_empty_string_for_empty_input():
    assert reverse_text("") == ""


def test_reverse_text_returns_same_single_character():
    assert reverse_text("a") == "a"


def test_reverse_text_keeps_letter_case_of_each_character():
    assert reverse_text("AbC") == "CbA"


def test_reverse_text_keeps_spaces_in_reversed_positions():
    assert reverse_text(" a b") == "b a "


def test_reverse_text_reverses_non_latin_text():
    assert reverse_text("привет") == "тевирп"


def test_reverse_text_applied_twice_returns_original():
    assert reverse_text(reverse_text("Hello, World!")) == "Hello, World!"


# ---------- count_vowels ----------

def test_count_vowels_returns_zero_for_empty_string():
    assert count_vowels("") == 0


def test_count_vowels_counts_lowercase_vowels():
    assert count_vowels("aeiou") == 5


def test_count_vowels_counts_uppercase_vowels():
    assert count_vowels("AEIOU") == 5


def test_count_vowels_ignores_case_in_mixed_text():
    assert count_vowels("Hello World") == 3


def test_count_vowels_returns_zero_for_text_without_vowels():
    assert count_vowels("bcdfg xyz") == 0


def test_count_vowels_does_not_treat_y_as_vowel():
    assert count_vowels("yY") == 0


def test_count_vowels_counts_repeated_vowels():
    assert count_vowels("aAaA") == 4


def test_count_vowels_ignores_non_english_vowels():
    assert count_vowels("аеиоу") == 0


def test_count_vowels_ignores_digits_and_punctuation():
    assert count_vowels("123 !?, e") == 1


# ---------- is_palindrome ----------

@pytest.mark.parametrize("text", ["racecar", "level", "abba"])
def test_is_palindrome_accepts_lowercase_palindromes(text):
    assert is_palindrome(text) is True


@pytest.mark.parametrize("text", ["Racecar", "Aba", "AbBa", "LEVEL"])
def test_is_palindrome_ignores_letter_case(text):
    assert is_palindrome(text) is True


@pytest.mark.parametrize("text", ["hello", "ab", "abca"])
def test_is_palindrome_rejects_non_palindromes(text):
    assert is_palindrome(text) is False


def test_is_palindrome_accepts_single_character():
    assert is_palindrome("a") is True


def test_is_palindrome_accepts_empty_string():
    # The contract does not name the empty string explicitly: an empty
    # string reads the same in both directions, so True is expected.
    assert is_palindrome("") is True


def test_is_palindrome_accepts_symmetric_spaces():
    assert is_palindrome("ab ba") is True


def test_is_palindrome_rejects_asymmetric_space():
    assert is_palindrome("ab a") is False


def test_is_palindrome_does_not_ignore_spaces():
    assert is_palindrome("a b a ") is False


def test_is_palindrome_accepts_symmetric_punctuation():
    assert is_palindrome("!a!") is True


def test_is_palindrome_does_not_ignore_punctuation():
    assert is_palindrome("a!a?") is False


def test_is_palindrome_rejects_phrase_whose_spaces_and_punctuation_matter():
    assert is_palindrome("A man, a plan, a canal: Panama") is False


# ---------- count_words ----------

def test_count_words_returns_zero_for_empty_string():
    assert count_words("") == 0


def test_count_words_returns_zero_for_spaces_only():
    assert count_words("     ") == 0


def test_count_words_returns_zero_for_tabs_and_newlines_only():
    assert count_words("\t\n \t") == 0


def test_count_words_counts_single_word():
    assert count_words("hello") == 1


def test_count_words_counts_words_separated_by_one_space():
    assert count_words("one two three") == 3


def test_count_words_counts_words_separated_by_tab():
    assert count_words("one\ttwo") == 2


def test_count_words_counts_words_separated_by_newline():
    assert count_words("one\ntwo") == 2


def test_count_words_counts_words_separated_by_mixed_whitespace():
    assert count_words("one \t\n two") == 2


def test_count_words_ignores_leading_trailing_and_repeated_spaces():
    assert count_words("  one   two  ") == 2


def test_count_words_counts_punctuated_token_as_one_word():
    assert count_words("Hello, world!") == 2


# ---------- remove_spaces ----------

def test_remove_spaces_removes_spaces_between_words():
    assert remove_spaces("a b c") == "abc"


def test_remove_spaces_returns_empty_string_for_empty_input():
    assert remove_spaces("") == ""


def test_remove_spaces_returns_empty_string_for_spaces_only():
    assert remove_spaces("   ") == ""


def test_remove_spaces_removes_leading_trailing_and_repeated_spaces():
    assert remove_spaces("  a  b ") == "ab"


def test_remove_spaces_returns_same_text_when_no_spaces():
    assert remove_spaces("abc") == "abc"


def test_remove_spaces_keeps_tab_character():
    assert remove_spaces("a\tb c") == "a\tbc"


def test_remove_spaces_keeps_newline_character():
    assert remove_spaces("a\nb c") == "a\nbc"


def test_remove_spaces_keeps_non_breaking_space():
    assert remove_spaces("a\u00a0b c") == "a\u00a0bc"


def test_remove_spaces_keeps_letter_case_and_punctuation():
    assert remove_spaces("Hi, You!") == "Hi,You!"
