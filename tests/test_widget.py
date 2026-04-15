import pytest

from src.widget import get_date, mask_account_card


# Тестирование маскировки номера карты
@pytest.mark.parametrize(
    "data, masked_data",
    [
        ("Visa Platinum 1596837868705199", "Visa Platinum 1596 83** **** 5199"),
        ("МИР 6831982476737658", "МИР 6831 98** **** 7658"),
        ("Счет 12341234123412349999", "Счет **9999"),
        ("привет", "Недопустимое значение"),
        ("Счет 12341234А2341234", "Недопустимое значение"),
        ("", "Пустая строка"),
    ],
)
def test_mask_account_card(data, masked_data):
    assert mask_account_card(data) == masked_data


def test_get_date():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
