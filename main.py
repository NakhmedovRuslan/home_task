from pathlib import Path

from src.generators import filter_by_currency, transaction_descriptions_by_keyword
from src.processing import filter_by_state, sort_by_date
from src.utils import operations
from src.utils_csv_excel import read_csv_file, read_excel_file
from src.widget import get_date, mask_account_card

BASE_DIR = Path(__file__).resolve().parent
json_file = BASE_DIR / "data" / "operations.json"
csv_file = BASE_DIR / "data" / "transactions.csv"
xlsx_file = BASE_DIR / "data" / "transactions_excel.xlsx"


def main():
    """Основная функция"""

    print("""Привет!
Добро пожаловать в программу работы с баковскими транзакциями.
Выбери необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
""")

    user_input = input("Введите цифру пункта меню: ")
    if user_input == "1":
        print("Для обработки выбран JSON-файл.")
        flag = True
        data = operations(json_file)
        filtered_data = None

        print("""Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")

        while True:
            user_choice = input("Введите EXECUTED, CANCELED или PENDING: ").lower().strip()
            if "executed" in user_choice:
                state = "EXECUTED"
                print('Операции отфильтрованы по статусу "EXECUTED"')
                break
            elif "canceled" in user_choice:
                state = "CANCELED"
                print('Операции отфильтрованы по статусу "CANCELED"')
                break
            elif "pending" in user_choice:
                state = "PENDING"
                print('Операции отфильтрованы по статусу "PENDING"')
                break
            else:
                print(f"Статус операции {user_choice} недоступен")

        filtered_data = filter_by_state(data, state)

        print("Отсортировать по возрастанию или по убыванию?")
        user_choice_sort_by_ascending = input("Введите по возрастанию или по убыванию: ").lower().strip()
        if user_choice_sort_by_ascending == "по убыванию":
            flag = False

        print("Отсортировать операции по дате? Да/Нет")
        user_choice_sort_by_date = input("Введите да или нет: ").lower().strip()
        if user_choice_sort_by_date == "да":
            filtered_data = sort_by_date(filtered_data, flag)

        print("Выводить только рублевые транзакции? Да/Нет")
        user_choice_sort_by_currency = input("Введите да или нет: ").lower().strip()
        if user_choice_sort_by_currency == "да":
            filtered_data = list(filter_by_currency(filtered_data))

        print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
        user_choice_sort_by_description = input("Введите да или нет: ").lower().strip()
        if user_choice_sort_by_description == "да":
            user_input_word = input("Введите ключевое слово: ").lower().strip()
            filtered_data = transaction_descriptions_by_keyword(filtered_data, user_input_word)

        print("Распечатываю итоговый список транзакций...\n")
        print(f"Всего банковских операций в выборке: {len(filtered_data)}\n")
        result = ""
        for elem in filtered_data:
            date = get_date(elem.get("date"))
            descr = elem.get("description")
            account_from = mask_account_card(elem.get("from"))
            account_to = mask_account_card(elem.get("to"))
            amount = elem.get("operationAmount").get("amount")
            currency = elem.get("operationAmount").get("currency").get("code")
            result += f"{date} {descr}\n{account_from}->{account_to}\nСумма: {amount} {currency}\n\n"
        return result

    elif user_input == "2":
        print("Для обработки выбран CSV-файл.")
        flag = True
        filtered_data = None

        print("""Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")

        while True:
            user_choice = input("Введите EXECUTED, CANCELED или PENDING: ").lower().strip()

            if "executed" in user_choice:
                state = "EXECUTED"
                print('Операции отфильтрованы по статусу "EXECUTED"')
                break

            elif "canceled" in user_choice:
                state = "CANCELED"
                print('Операции отфильтрованы по статусу "CANCELED"')
                break

            elif "pending" in user_choice:
                state = "PENDING"
                print('Операции отфильтрованы по статусу "PENDING"')
                break

            else:
                print(f"Статус операции {user_choice} недоступен")

        filtered_data = read_csv_file(csv_file, state)

        print("Отсортировать по возрастанию или по убыванию?")
        user_choice_sort_by_ascending = input("Введите по возрастанию или по убыванию: ").lower().strip()

        if user_choice_sort_by_ascending == "по убыванию":
            flag = False

        print("Отсортировать операции по дате? Да/Нет")
        user_choice_sort_by_date = input("Введите да или нет: ").lower().strip()

        if user_choice_sort_by_date == "да":
            filtered_data = sort_by_date(filtered_data, flag)

        print("Выводить только рублевые транзакции? Да/Нет")
        user_choice_sort_by_currency = input("Введите да или нет: ").lower().strip()
        if user_choice_sort_by_currency == "да":
            filtered_data = list(filter_by_currency(filtered_data))

        print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
        user_choice_sort_by_description = input("Введите да или нет: ").lower().strip()
        if user_choice_sort_by_description == "да":
            user_input_word = input("Введите ключевое слово: ").lower().strip()
            filtered_data = transaction_descriptions_by_keyword(filtered_data, user_input_word)

        print("Распечатываю итоговый список транзакций...\n")
        print(f"Всего банковских операций в выборке: {len(filtered_data)}\n")

        result = ""

        for elem in filtered_data:
            date = get_date(elem.get("date"))
            descr = elem.get("description")

            account_from = mask_account_card(elem.get("from")) if elem.get("from") else ""
            account_to = mask_account_card(elem.get("to")) if elem.get("to") else ""

            amount = elem.get("amount")
            currency = elem.get("currency_name")

            result += f"{date} {descr}\n" f"{account_from}->{account_to}\n" f"Сумма: {amount} {currency}\n\n"

        return result

    elif user_input == "3":
        print("Для обработки выбран XLSX-файл.")
        flag = True
        filtered_data = None

        print("""Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")

        while True:
            user_choice = input("Введите EXECUTED, CANCELED или PENDING: ").lower().strip()

            if "executed" in user_choice:
                state = "EXECUTED"
                print('Операции отфильтрованы по статусу "EXECUTED"')
                break

            elif "canceled" in user_choice:
                state = "CANCELED"
                print('Операции отфильтрованы по статусу "CANCELED"')
                break

            elif "pending" in user_choice:
                state = "PENDING"
                print('Операции отфильтрованы по статусу "PENDING"')
                break

            else:
                print(f"Статус операции {user_choice} недоступен")

        filtered_data = read_excel_file(xlsx_file, state)

        print("Отсортировать по возрастанию или по убыванию?")
        user_choice_sort_by_ascending = input("Введите по возрастанию или по убыванию: ").lower().strip()

        if user_choice_sort_by_ascending == "по убыванию":
            flag = False

        print("Отсортировать операции по дате? Да/Нет")
        user_choice_sort_by_date = input("Введите да или нет: ").lower().strip()

        if user_choice_sort_by_date == "да":
            filtered_data = sort_by_date(filtered_data, flag)

        print("Выводить только рублевые транзакции? Да/Нет")
        user_choice_sort_by_currency = input("Введите да или нет: ").lower().strip()
        if user_choice_sort_by_currency == "да":
            filtered_data = list(filter_by_currency(filtered_data))

        print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
        user_choice_sort_by_description = input("Введите да или нет: ").lower().strip()
        if user_choice_sort_by_description == "да":
            user_input_word = input("Введите ключевое слово: ").lower().strip()
            filtered_data = transaction_descriptions_by_keyword(filtered_data, user_input_word)

        print("Распечатываю итоговый список транзакций...\n")
        print(f"Всего банковских операций в выборке: {len(filtered_data)}\n")

        result = ""

        for elem in filtered_data:
            date = get_date(elem.get("date"))
            descr = elem.get("description")

            account_from = mask_account_card(elem.get("from")) if elem.get("from") else ""
            account_to = mask_account_card(elem.get("to")) if elem.get("to") else ""

            amount = elem.get("amount")
            currency = elem.get("currency_name")

            result += f"{date} {descr}\n" f"{account_from}->{account_to}\n" f"Сумма: {amount} {currency}\n\n"

        return result


if __name__ == "__main__":
    print(main())
