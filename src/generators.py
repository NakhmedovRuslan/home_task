from typing import Generator


def filter_by_currency(data: list, currency: str = "USD") -> Generator[str, dict]:
    """Функция возвращает отфильтрованный список транзакций по валюте"""
    if not data:
        yield "Нет данных"
    else:
        filter_transactions = (
            transaction for transaction in data if transaction["operationAmount"]["currency"]["code"] == currency
        )
        for elem in filter_transactions:
            yield elem


def transaction_descriptions(data: list) -> Generator[str]:
    """Функция возвращает описание каждой операции из списка транзакций по очереди"""
    if not data:
        yield "Нет данных"
    else:
        filter_descriptions = (description for description in data if description.get("description"))
        for elem in filter_descriptions:
            yield elem["description"]


def card_number_generator(start: int, finish: int) -> Generator[str]:
    """Функция генерирует номер карты по заданному диапазону start и stop"""
    if start <= finish:
        for number in range(start, finish + 1):
            num_to_str = str(number)

            mask_symbols = 16 - len(num_to_str)
            full_number = "X" * mask_symbols + num_to_str
            formated_number = " ".join(full_number[i : i + 4] for i in range(0, 16, 4))
            yield formated_number
    else:
        yield "Некорректные данные"
