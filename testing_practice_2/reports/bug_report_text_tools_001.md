ID: TEXT-001
Название: is_palindrome не игнорирует регистр символов
Модуль и версия/коммит: text_tools.py, исходная версия из коммита bc0c325 (viktorhtp, "Create text_tools.py")
Автор: Витя
Тестировщик: Артем
Шаги или вызов функции: вызвать is_palindrome("Racecar"), is_palindrome("Aba"), is_palindrome("AbBa")
Ожидаемый результат: True для всех трёх вызовов (контракт: регистр символов полностью игнорируется)
Фактический результат: False для всех трёх вызовов (строка сравнивается с обратной без приведения к одному регистру)
Название падающего теста: tests/test_text_tools.py::test_is_palindrome_ignores_letter_case[Racecar]; ::[Aba]; ::[AbBa]
Серьёзность (Blocker/Critical/Major/Minor/Trivial): Major
Итоговый статус: Closed

Среда: Python 3.12.3, pytest, pytest-cov.
Команда запуска исходной версии (text_tools.py из bc0c325 + tests/test_text_tools.py):
python -m pytest tests/test_text_tools.py --cov=text_tools --cov-report=term-missing

Результат: 53 теста, 50 прошли, 3 упали. Покрытие операторов text_tools.py: 100% (11/11).
Остальные 4 функции (reverse_text, count_vowels, count_words, remove_spaces) ведут себя по контракту.
Тест test_is_palindrome_ignores_letter_case[LEVEL] проходит и на ошибочной версии,
так как строка симметрична и без учёта регистра, поэтому он не вскрывает дефект.

Исправление: Витя изменил is_palindrome (коммит 8a9b03d) — строка приводится к нижнему
регистру перед сравнением с обратной строкой.
Повторная проверка (Артем): text_tools.py из коммита 8a9b03d, весь набор tests/test_text_tools.py:
53 теста, 53 прошли, 0 упали, покрытие 100% (12/12). Все три ранее падавших теста проходят.
Дефект подтверждён как исправленный, статус — Closed.
