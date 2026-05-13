import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")  # API ключ из файла .env


def transaction_convert(data: dict) -> float:
    """Возвращает сумму транзакции в рублях"""

    headers = {"apikey": f"{API_KEY}"}

    if data["operationAmount"]["currency"]["code"] == "RUB":  # Проверка, если валюта- RUB, возвращает значение
        return float(data["operationAmount"]["amount"])

    params = {
        "to": "RUB",
        "from": data["operationAmount"]["currency"]["code"],
        "amount": data["operationAmount"]["amount"],
    }

    url = "https://api.apilayer.com/exchangerates_data/convert"

    response = requests.get(url, headers=headers, params=params)
    converted_data = response.json()

    return float(converted_data["result"])


if __name__ == "__main__":
    transaction = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    }

    print(transaction_convert(transaction))
