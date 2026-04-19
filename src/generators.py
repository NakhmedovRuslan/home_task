def filter_by_currency(data, currency="USD"):
    filter_transactions = (transaction for transaction in data if transaction["operationAmount"]["currency"]["code"] == currency)
    for elem in filter_transactions:
        yield elem


def transaction_descriptions(data):
    filter_descriptions = (description for description in data if description["description"])
    for elem in filter_descriptions:
        yield elem["description"]


def card_number_generator(start, finish):
    for number in range(start, finish + 1):
        num_to_str = str(number)

        mask_symbols = 16 - len(num_to_str)
        full_number = "X" * mask_symbols + num_to_str

        formated_number = " ".join(full_number[i:i + 4] for i in range(0, 16, 4))

        yield formated_number

transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]

result_cur = filter_by_currency(transactions, "USD")
for element in result_cur:
    print(element)

result_des = transaction_descriptions(transactions)
for elem in result_des:
    print(elem)

for card_number in card_number_generator(1, 5):
    print(card_number)