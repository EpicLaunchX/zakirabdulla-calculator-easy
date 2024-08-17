from unittest.mock import patch

import pytest

from src.pytemplate.entrypoints.cli.main import main


@patch("builtins.input", return_value="1,2,add")
def test_main_add(mock_input):
    result = main()
    assert result == 3


@patch("builtins.input", return_value="2,1,subtract")
def test_main_subtract(mock_input):
    result = main()
    assert result == 1


@patch("builtins.input", return_value="2,3,multiply")
def test_main_multiply(mock_input):
    result = main()
    assert result == 6


@patch("builtins.input", return_value="6,3,divide")
def test_main_divide(mock_input):
    result = main()
    assert result == 2


@patch("builtins.input", return_value="6,3,invalid")
def test_main_invalid(mock_input):
    with pytest.raises(ValueError):
        main()
