import pytest

from src.pytemplate.domain.models import Operands, operands_factory
from src.pytemplate.service.calculator import Calculator


def test_calculator_add():
    result = Calculator().add(Operands(1, 2))
    assert result == 3
    assert type(result) == int


def test_calculator_subtract():
    result = Calculator().subtract(Operands(2, 1))
    assert result == 1
    assert type(result) == int


def test_calculator_multiply():
    result = Calculator().multiply(Operands(2, 3))
    assert result == 6
    assert type(result) == int


def test_calculator_divide():
    result = Calculator().divide(Operands(6, 3))
    assert result == 2
    assert type(result) == int
