import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "data_cards, masked_data_card",
    [
        ("1596837868705199", "1596 83** **** 5199"),
        ("6831982476737658", "6831 98** **** 7658"),
    ],
)
def test_get_mask_card_number(data_cards, masked_data_card):
    """Функция для тестирования маскировки номера карты"""
    assert get_mask_card_number(data_cards) == masked_data_card


@pytest.mark.parametrize(
    "data_account, masked_data_account",
    [
        ("79461259795423164329", "**4329"),
        ("12341234456778901234", "**1234"),
    ],
)
def test_get_mask_account(data_account, masked_data_account):
    """Функция для тестирования маскировки номера счета"""
    assert get_mask_account(data_account) == masked_data_account
