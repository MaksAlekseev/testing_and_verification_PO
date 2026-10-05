import pytest
from calculator import add, subtract, multiply, divide, absolute_value

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(-5, -5) == -10
    assert add(2.5, 2.5) == 5.0

def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(0, 5) == -5
    assert subtract(-5, -5) == 0
    assert subtract(5.5, 2.0) == 3.5

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 3) == -6
    assert multiply(0, 10) == 0
    assert multiply(1.5, 2.0) == 3.0

def test_divide():
    assert divide(10, 2) == 5.0
    assert divide(-10, 2) == -5.0
    assert divide(5, 2) == 2.5
    # Проверка, что при делении на ноль вызывается исключение ZeroDivisionError
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

def test_absolute_value():
    assert absolute_value(5) == 5
    assert absolute_value(0) == 0
    # aссерт упадет, потому что функция вернет -5 вместо 5
    assert absolute_value(-5) == 5 
    assert absolute_value(-3.5) == 3.5
