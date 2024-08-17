import pytest

from src.pytemplate.domain.models import Operands, operands_factory
from src.pytemplate.service.calculator import Calculator


def test_calculator_add():
    result = Calculator().add(operands_factory(1, 2))
    assert result == 3
    assert type(result) == int


def test_calculator_subtract():
    result = Calculator().subtract(operands_factory(2, 1))
    assert result == 1
    assert type(result) == int


def test_calculator_multiply():
    result = Calculator().multiply(operands_factory(2, 3))
    assert result == 6
    assert type(result) == int


def test_calculator_divide():
    result = Calculator().divide(operands_factory(6, 3))
    assert result == 2
    assert type(result) == int
