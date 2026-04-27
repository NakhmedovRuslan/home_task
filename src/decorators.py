from functools import wraps
from typing import Any, Callable


def log(filename: str | None = None) -> Callable[[Callable], Callable]:
    def log_2_stage(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                status = "OK"
            except Exception as e:
                status = "ERROR"
                error = e
                error_text = str(error)

            if not filename:
                print("---------------------------------------------------\n")
                print(f"function {func.__name__} with args: args - {args}, kwargs - {kwargs}\n")
                if status == "OK":
                    print(f"Result: {status} - {result}\n")
                else:
                    print(f"Result: {status} - {type(error).__name__}: {error_text}\n")
                print("---------------------------------------------------\n")

            else:
                with open(f"../{filename}", "a", encoding="UTF-8") as file:
                    file.write("---------------------------------------------------\n")
                    file.write(f"function {func.__name__} with args: args - {args}, kwargs - {kwargs}\n")
                    if status == "OK":
                        file.write(f"Result: {status} - {result}\n")
                    else:
                        file.write(f"Result: {status} - {type(error).__name__}: {error_text}\n")
                    file.write("---------------------------------------------------\n")

            if status == "ERROR":
                raise error

            return result

        return wrapper

    return log_2_stage


@log(filename="mylog.txt")
def my_function(x: int | float, y: int | float) -> int | float:
    """Функция складывает 2 числа и выдает результат"""
    return x + y


print(my_function(1, 2))
