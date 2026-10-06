Проверка исправления LIST-001

Проверялась версия list_tools.py из main commit f8684c35e8020b7ef93ce1cc3bfa5a822018d22c.
Среда: Python 3.12.5, pytest 9.1.1, pytest-cov 7.1.0.

Из testing_practice_2 выполнены команды:
python -m pytest tests/test_list_tools.py --cov=list_tools --cov-report=term-missing
Результат: 24 passed; list_tools.py — покрытие 100% (29/29 операторов).

python -m pytest --cov=. --cov-report=term-missing
Результат полного набора: 106 passed; общее покрытие — 100% (276/276 операторов).

Оба ранее падавших теста прошли. LIST-001 закрыт.
