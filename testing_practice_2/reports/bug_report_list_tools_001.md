ID: LIST-001
Название: max_number возвращает неверный максимум для списков с отрицательными числами
Модуль и версия/коммит: list_tools.py, main commit ae41962430b88a2542fc6e448baa8c1070582413
Автор: Артем
Тестировщик: Катя
Шаги или вызов функции: вызвать max_number([-5, -2, -9]) и max_number([-4])
Ожидаемый результат: -2 для первого вызова и -4 для второго
Фактический результат: 0 для обоих вызовов
Название падающего теста: test_max_number_handles_list_with_only_negative_values; test_max_number_handles_single_item
Серьёзность (Blocker/Critical/Major/Minor/Trivial): Major
Статус (Open/Fixed/Closed): Open
