def reverse_text(text: str) -> str:
    return text[::-1]

def count_vowels(text: str) -> int:
    vowels = set("aeiou")
    return sum(1 for char in text.lower() if char in vowels)

def is_palindrome(text: str) -> bool:
    """
    Проверяет палиндром, игнорируя регистр, но учитывая пробелы и знаки.
    """
    text_lower = text.lower()
    return text_lower == text_lower[::-1]

def count_words(text: str) -> int:
    return len(text.split())

def remove_spaces(text: str) -> str:
    return text.replace(" ", "")
