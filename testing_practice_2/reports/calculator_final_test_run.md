# Повторная проверка `calculator.py`

**Тестировщик:** Витя. **Среда:** Windows, Python 3.12.10, pytest 9.1.1, pytest-cov 7.1.0.

```powershell
python -m pytest tests/test_calculator.py --cov=calculator --cov-report=term-missing
```

**Результат Вити:** 5 passed; покрытие `calculator.py` — 100% (10/10 операторов). Проверка подтвердила исправление `BUG-CALC-001`.

После приведения аннотаций и документации `add` к финальному виду Максим повторно выполнил ту же команду в Windows, Python 3.12.5: **5 passed**, покрытие — **100% (10/10)**.
