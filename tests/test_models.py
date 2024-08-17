import pytest

from src.pytemplate.domain.models import Operands, operands_factory


def test_model_created():
    operands = Operands(first_operand=1, second_operand=2)
    assert operands.first_operand == 1
    assert operands.second_operand == 2


def test_factory_created():
    operands = operands_factory(1, 2)
    assert isinstance(operands, Operands)
    assert type(operands) == Operands
