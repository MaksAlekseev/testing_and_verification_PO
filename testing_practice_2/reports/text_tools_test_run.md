# Прогон тестов модуля text_tools.py (тестировщик: Артем)

## Прогон 1. Исходная версия Вити (коммит bc0c325)

Среда: Python 3.12.3, pytest, pytest-cov. Команда:

```
python -m pytest tests/test_text_tools.py --cov=text_tools --cov-report=term-missing
```

Результат: **53 теста, 50 прошли, 3 упали**. Покрытие операторов: 100% (11/11).
Падают только `test_is_palindrome_ignores_letter_case[Racecar]`, `[Aba]`, `[AbBa]`.
Описание дефекта — в `bug_report_text_tools_001.md` (TEXT-001, статус Open).

Фрагмент фактического вывода:

```
text_tools.py      11      0   100%
---------------------------------------------
TOTAL              11      0   100%
=========================== short test summary info ============================
FAILED tests/test_text_tools.py::test_is_palindrome_ignores_letter_case[Racecar]
FAILED tests/test_text_tools.py::test_is_palindrome_ignores_letter_case[Aba]
FAILED tests/test_text_tools.py::test_is_palindrome_ignores_letter_case[AbBa]
3 failed, 50 passed in 0.16s
```

Ограничение: Витя исправил `is_palindrome` (коммит 8a9b03d) раньше, чем получил
баг-репорт, поэтому прогон исходной версии выполнен по сохранённому коммиту bc0c325.

## Прогон 2. Исправленная версия Вити (коммит 8a9b03d)

Та же команда, тот же набор тестов (тесты не менялись и не ослаблялись):

```
python -m pytest tests/test_text_tools.py --cov=text_tools --cov-report=term-missing
```

Результат: **53 теста, 53 прошли, 0 упали**. Покрытие операторов: 100% (12/12).
Фактический вывод:

```
.....................................................                    [100%]
_______________ coverage: platform linux, python 3.12.3-final-0 ________________

Name            Stmts   Miss  Cover   Missing
---------------------------------------------
text_tools.py      12      0   100%
---------------------------------------------
TOTAL              12      0   100%
53 passed in 0.15s
```

Вывод: TEXT-001 исправлен, баг-репорт закрыт (Closed). Новых дефектов в
`reverse_text`, `count_vowels`, `count_words` и `remove_spaces` не найдено.
