import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency_usd(test_data_usd):
    """Функция тестирует фильтрация по валюте USD"""
    result = list(filter_by_currency(test_data_usd, "USD"))

    assert (transaction["operationAmount"]["currency"]["code"] == "USD" for transaction in result)


def test_filter_by_currency_rub(test_data_rub):
    """Функция тестирует фильтрация по валюте RUB"""
    result = list(filter_by_currency(test_data_rub, "RUB"))

    assert (transaction["operationAmount"]["currency"]["code"] == "RUB" for transaction in result)


def test_filter_by_currency_other(test_data):
    """Функция тестирует фильтрация по валюте отличной от RUB и USD"""
    result = list(filter_by_currency(test_data, "EUR"))

    assert result == []


def test_filter_by_currency_empty(test_data_empty):
    """Функция тестирует фильтрация по пустому списку"""
    result = list(filter_by_currency(test_data_empty))

    assert result == ["Нет данных"]


def test_transaction_descriptions_empty(test_data_empty):
    """Функция тестирует возврат описания операций при пустом списке"""
    result = list(transaction_descriptions(test_data_empty))
    assert result == ["Нет данных"]


def test_transaction_descriptions(test_data):
    """Функция тестирует возврат описания операций"""
    result = list(transaction_descriptions(test_data))
    assert result == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]


@pytest.mark.parametrize(
    "start, finish, expected",
    [
        (
            1,
            3,
            [
                "XXXX XXXX XXXX XXX1",
                "XXXX XXXX XXXX XXX2",
                "XXXX XXXX XXXX XXX3",
            ],
        ),
        (
            9999,
            10000,
            [
                "XXXX XXXX XXXX 9999",
                "XXXX XXXX XXX1 0000",
            ],
        ),
        (
            3,
            3,
            [
                "XXXX XXXX XXXX XXX3",
            ],
        ),
        (
            2,
            1,
            [
                "Некорректные данные",
            ],
        ),
    ],
)
def test_card_number_generator(start, finish, expected):
    """Функция тестирует генератор номеров карт"""
    result = list(card_number_generator(start, finish))
    assert result == expected
