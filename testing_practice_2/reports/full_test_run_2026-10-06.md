# Сводный тестовый прогон, 2026-10-06

Среда: Python 3.12.5, pytest 9.1.1, pytest-cov 7.1.0.

Команда из `testing_practice_2`:

```powershell
python -m pytest tests/test_calculator.py tests/test_list_tools.py tests/test_number_checks.py --cov=calculator --cov=list_tools --cov=number_checks --cov-report=term-missing
```

Результат: **49 passed, 2 failed из 51**. Упали только проверки обработки
отрицательных списков:

- `test_max_number_handles_list_with_only_negative_values`: ожидалось `-2`,
  получено `0`.
- `test_max_number_handles_single_item`: ожидалось `-4`, получено `0`.

Обе ошибки соответствуют открытому дефекту `LIST-001` в модуле Артема.
`calculator.py`: 100% (10/10 statements), `list_tools.py`: 100% (29/29),
`number_checks.py`: 100% (12/12), итого 100% покрытия операторов (51/51).
Покрытие не означает прохождение всех проверок.

Тесты `text_tools.py` не включены: `tests/test_text_tools.py` в репозитории пока
нет. Мутационные итоги не включены: текущие запуски MutPy 0.6.1 дали
недостоверную статистику (0 покрытых узлов при 24 выполненных тестах и выживший
мутант, который должен нарушить тест); для практики нужен повтор валидным методом.
