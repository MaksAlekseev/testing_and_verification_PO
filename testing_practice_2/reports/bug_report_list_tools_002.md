ID: LIST-002
Название: Максимум для одноэлементного отрицательного списка возвращается неверно
Модуль и версия/коммит: list_tools.py, main commit ae41962430b88a2542fc6e448baa8c1070582413
Автор: Артем
Тестировщик: Катя
Шаги или вызов функции: max_number([-4])
Ожидаемый результат: -4
Фактический результат: 0
Название падающего теста: test_max_number_handles_single_item
Серьёзность (Blocker/Critical/Major/Minor/Trivial): Major
Статус (Open/Fixed/Closed): Open
