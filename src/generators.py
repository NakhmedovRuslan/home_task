from typing import Generator


def filter_by_currency(data: list, currency: str = "RUB") -> Generator[dict, None, None]:
    """Функиця фильтрует список по валюте"""
    if not data:
        return

    for transaction in data:
        if not transaction:
            continue

        curr = transaction.get("operationAmount", {}).get("currency", {}).get("code")

        if not curr:
            curr = transaction.get("currency_code")

        if not curr:
            continue

        if str(curr).strip().upper() == currency.upper():
            yield transaction


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


def transaction_descriptions_by_keyword(data: list, keyword: str = "") -> list:
    """Фильтрация транзакций по ключевому слову в описании"""

    if not data:
        return []

    list_transactions = []

    for elem in data:
        description = elem.get("description", "").lower()

        if keyword.lower() in description:
            list_transactions.append(elem)

    return list_transactions


# if __name__ == '__main__':
#
#     transactions = [
#         {
#             "id": 441945886,
#             "state": "EXECUTED",
#             "date": "2019-08-26T10:50:58.294041",
#             "operationAmount": {
#                 "amount": "31957.58",
#                 "currency": {
#                     "name": "руб.",
#                     "code": "RUB"
#                 }
#             },
#             "description": "Перевод организации",
#             "from": "Maestro 1596837868705199",
#             "to": "Счет 64686473678894779589"
#         },
#         {
#             "id": 142264268,
#             "state": "EXECUTED",
#             "date": "2019-04-04T23:20:05.206878",
#             "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
#             "description": "Перевод со счета на счет",
#             "from": "Счет 19708645243227258542",
#             "to": "Счет 75651667383060284188",
#         },
#         {
#             "id": 873106923,
#             "state": "EXECUTED",
#             "date": "2019-03-23T01:09:46.296404",
#             "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
#             "description": "Перевод со счета на счет",
#             "from": "Счет 44812258784861134719",
#             "to": "Счет 74489636417521191160",
#         }
#         ]
#
#
#
#     # print(transaction_descriptions_by_keyword(transactions, keyword="перевод организации"))
