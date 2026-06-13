import re
from collections import Counter
from typing import Any


def process_bank_search(data: list[dict], search: str) -> list[dict[str, Any]]:
    """Функция ищет по ключевому слову значение из описания траназакции"""
    pattern = re.compile(search, re.IGNORECASE)

    result = [elem for elem in data if pattern.findall(elem.get("description"))]
    return result


def process_bank_operations(data: list[dict], categories: list[str]) -> dict[str, list[str]]:
    """Функция считает совпадения в списке по описанию транзакции"""
    counted = Counter()
    for operation in data:
        description = operation.get("description")
        if description in categories:
            counted[description] += 1

    return dict(counted)


data = [
    {
        "id": 650703.0,
        "description": "Перевод организации",
    },
    {
        "id": 525262.0,
        "description": "Перевод с карты на карту",
    },
    {
        "id": 3598919.0,
        "description": "Перевод с карты на карту",
    },
    {
        "id": 366176.0,
        "description": "Оплата услуг",
    },
]

categories = ["Перевод с карты на карту", "Оплата услуг"]

# print(process_bank_search(data, "ОпЛаТа"))
# print(process_bank_operations(data, categories))
