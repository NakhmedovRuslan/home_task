import pytest

from src.decorators import log


def test_log_in_file_success():
    @log(filename="mylog.txt")
    def my_function(x, y):
        """Функция складывания двух чисел"""
        return x + y

    result = my_function(1, 2)
    assert result == 3
    with open("mylog.txt", "a", encoding="UTF-8") as file:
        file.write("function my_function with args:\n")
        file.write("Result:\n")


def test_log_in_file_fail():
    @log(filename="mylog.txt")
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
    assert ("my_function" in captured.out) and ("args - (1, 2)" in captured.out)

    with pytest.raises(TypeError, match="unsupported operand"):
        my_function(1, "0")
        captured = capsys.readouterr()
        assert ("my_function" in captured.out) and ("args - (1, '0')" in captured.out)

    my_function(1, 2)
    assert my_function(1, 2) == 3
