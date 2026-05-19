import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("./logs/masks.log", encoding="utf-8", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str:
    """Функция маскирующая символы номера карты"""
    logger.debug(f"Функция get_mask_card_number запущена с аргументом: {card_number}")
    masked_number = card_number[:6] + "******" + card_number[-4:]
    separated_numbers = []
    for elem in range(0, len(masked_number), 4):
        separated_numbers.append(masked_number[elem : elem + 4])

    result = " ".join(separated_numbers)
    logger.debug(f"Результат работы функции get_mask_card_number: {result}")
    return result


def get_mask_account(account_number: str) -> str:
    """Функция маскирующая номер счёта"""
    logger.debug(f"Функция get_mask_account запущена с аргументом: {account_number}")
    masked_account = "**" + account_number[-4:]
    logger.debug(f"Результат работы функции get_mask_card_number: {masked_account}")
    return masked_account


if __name__ == "__main__":
    print(get_mask_card_number("1111222233334445"))
    print(get_mask_account("11111222223333344445"))
