"""Tests for Calculator class."""

import pytest
from mathcalc.calculator import Calculator


def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0


def test_subtract():
    calc = Calculator()
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(0, 5) == -5


def test_multiply():
    calc = Calculator()
    assert calc.multiply(3, 4) == 12
    assert calc.multiply(-2, 3) == -6


def test_divide():
    calc = Calculator()
    assert calc.divide(10, 2) == 5
    assert calc.divide(7, 2) == 3.5


def test_divide_by_zero():
    calc = Calculator()
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.divide(5, 0)


def test_power():
    calc = Calculator()
    assert calc.power(2, 3) == 8
    assert calc.power(5, 0) == 1
    assert calc.power(2, -2) == 0.25
    assert calc.power(4, 0.5) == 2.0


def test_sqrt():
    calc = Calculator()
    assert calc.sqrt(16) == 4.0
    assert calc.sqrt(2) == pytest.approx(1.414, rel=0.001)
    assert calc.sqrt(0) == 0


def test_sqrt_negative():
    calc = Calculator()
    with pytest.raises(ValueError, match="Cannot calculate square root of negative number"):
        calc.sqrt(-1)
