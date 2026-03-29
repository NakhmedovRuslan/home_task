def get_mask_card_number(card_number: str) -> str:
    """Функция маскирующая символы номера карты"""

    masked_number = card_number[:7] + "*****" + card_number[-4:]
    separated_numbers = []
    for elem in range(0, len(masked_number), 4):
        separated_numbers.append(masked_number[elem : elem + 4])

    result = " ".join(separated_numbers)
    return result


def get_mask_account(account_number: str) -> str:
    """Функция маскирующая номер счёта"""

    masked_account = "**" + account_number[-4:]
    return masked_account
