def filter_by_state(received_data: list, state: str = "EXECUTED") -> list:
    """Функция фильтрует транзакции по статусам. По умолчанию - по выполненным"""
    sorted_by_state = []

    for elem in received_data:

        if elem["state"] == state:
            sorted_by_state.append(elem)

    return sorted_by_state


def sort_by_date(received_data: list, reverse: bool = True) -> list:
    """Функция сортирует транзакции по дате"""
    sorted_by_date = sorted(received_data, key=lambda x: x["date"], reverse=reverse)

    return sorted_by_date