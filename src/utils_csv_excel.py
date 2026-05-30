from pathlib import Path

import pandas as pd


def read_csv_file(filename: Path, state: str = "") -> list[dict] | str:
    """Функция читает csv файл и возвращает строки отфильтрованные по статусу транзакции"""
    try:
        df = pd.read_csv(filename, delimiter=";")
        state_sort = df.loc[df.state == state].to_dict(orient="records")

        return state_sort

    except FileNotFoundError:
        return "File not found"


def read_excel_file(filename: Path, state: str = "") -> pd.DataFrame:
    """Функция читает excel файл и возвращает строки отфильтрованные по статусу транзакции"""
    try:
        df = pd.read_excel(filename)
        state_sort = df.loc[df.state == state].to_dict(orient="records")
        return state_sort

    except FileNotFoundError:
        return "File not found"


# BASE_DIR = Path(__file__).resolve().parent.parent
# CSV_FILE = BASE_DIR / "data" / "transactions.csv"
# EXCEL_FILE = BASE_DIR / "data" / "transactions_excel.xlsx"
# print(read_csv_file(CSV_FILE, state="EXECUTED"))
# print(read_excel_file(EXCEL_FILE, state="CANCELED"))
