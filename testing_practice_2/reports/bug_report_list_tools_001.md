ID: LIST-001
Название: Максимум неверно вычисляется для списка отрицательных чисел
Модуль и версия/коммит: list_tools.py, main commit ae41962430b88a2542fc6e448baa8c1070582413
Автор: Артем
Тестировщик: Катя
Шаги или вызов функции: max_number([-5, -2, -9])
Ожидаемый результат: -2
Фактический результат: 0
Название падающего теста: test_max_number_handles_list_with_only_negative_values
Серьёзность (Blocker/Critical/Major/Minor/Trivial): Major
Статус (Open/Fixed/Closed): Open
