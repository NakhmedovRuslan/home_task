import pytest

from src.decorators import log


def test_log_in_file_success(tmp_path):
    file = tmp_path / "test.txt"
    @log(filename=file)
    def my_function(x, y):
        """Функция складывания двух чисел"""
        return x + y

    result = my_function(1, 2)
    assert result == 3
    with open(file, "r", encoding="UTF-8") as f:
        read = f.readlines()
        assert read[-2] == "Result: OK - 3\n"


def test_log_in_file_fail(tmp_path):
    file = tmp_path / "test.txt"
    @log(filename=file)
    def my_function(x, y):
        """Функция складывания двух чисел"""
        return x + y

    with pytest.raises(Exception, match="unsupported operand"):
        result = my_function(1, "2")
        print(result)


def test_log_in_console(capsys):
    @log(filename="")
    def my_function(x, y):
        """Функция складывания двух чисел"""
        return x + y

    my_function(1, 2)
    captured = capsys.readouterr()
    assert "function my_function with args: args - (1, 2), kwargs - {}" in captured.out

    with pytest.raises(TypeError, match="unsupported operand"):
        my_function(1, "0")

    my_function(1, 2)
    assert my_function(1, 2) == 3
