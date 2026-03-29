from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(information: str) -> str:
    """Функция маскирующая номер карты или счёта"""

    splited_information = information.split()
    card_or_account_info = " ".join(splited_information[:-1])
    number = splited_information[-1]

    if "счет" in card_or_account_info.lower():
        masked_number = get_mask_account(number)
    else:
        masked_number = get_mask_card_number(number)

    return f"{card_or_account_info} {masked_number}"


user_input = input("Введите информацию о счёте или карте: ")
print(mask_account_card(user_input))


def get_date(date: str) -> str:
    """Функция преобразующая введенную дату в формат ДД.ММ.ГГГГ"""
    year = date[:4]
    month = date[5:7]
    day = date[8:10]
    actual_date = f"{day}.{month}.{year}"

    return actual_date


print(get_date("2024-03-11T02:26:18.671407"))
