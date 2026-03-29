def get_mask_card_number(card_number: str) -> str:
    """Функция маскирующая символы номера карты"""

    # if not card_number.isdigit():
    # return "[Ошибка] Введите номер карты цифрами, без пробелов."

    # if len(card_number) != 16:
    # print("[Ошибка] Вы ввели некорректный номер карты. Должно быть 16 цифр.")

    masked_number = card_number[:7] + "*****" + card_number[-4:]
    separated_numbers = []
    for elem in range(0, len(masked_number), 4):
        separated_numbers.append(masked_number[elem : elem + 4])

    result = " ".join(separated_numbers)
    return result


def get_mask_account(account_number: str) -> str:
    """Функция маскирующая номер счёта"""

    # if not account_number.isdigit():
    # return "[Ошибка] Введите номер счёта цифрами, без пробелов."

    # if len(account_number) != 20:
    # return "[Ошибка] Вы ввели некорректный номер карты. Должно быть 20 цифр."

    masked_account = "**" + account_number[-4:]
    return masked_account


# user_card_number = input("Введите номер карты: ")
# user_account = input("Введите номер счёта: ")

# print(get_mask_card_number(user_card_number))
# print(get_mask_account(user_account))
