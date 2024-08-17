from unittest import mock

import pytest

from src.pytemplate.entrypoints.cli.main import main


def test_main_add():
    with mock.patch("builtins.input", return_value="1,2,add") as mock_result:
        result = main()
        assert result == 3


def test_main_subtract():
    with mock.patch("builtins.input", return_value="2,1,subtract"):
        result = main()
        assert result == 1


def test_main_multiply():
    with mock.patch("builtins.input", return_value="2,3,multiply"):
        result = main()
        assert result == 6


def test_main_divide():
    with mock.patch("builtins.input", return_value="6,3,divide") as mock_result:
        result = main()
        assert result == 2


def test_main_invalid():
    with mock.patch("builtins.input", return_value="6,3,invalid") as mock_result:
        with pytest.raises(ValueError):
            main()
