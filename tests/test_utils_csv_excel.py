from unittest.mock import patch

import pandas as pd

from src.utils_csv_excel import read_csv_file, read_excel_file


def test_read_csv_file_without_file():
    result = read_csv_file("fake_csv_file.csv")
    assert result == "File not found"


def test_read_excel_file_without_file():
    result = read_excel_file("fake_excel_file.xlsx")
    assert result == "File not found"


@patch("src.utils_csv_excel.pd.read_csv")
def test_read_csv_file(mock_read_csv_file):
    df = pd.DataFrame({"id": ["650703", "593027"], "state": ["EXECUTED", "CANCELED"]})

    mock_read_csv_file.return_value = df
    result = read_csv_file("fake_csv_file.csv", state="EXECUTED")

    assert result.iloc[0]["id"] == "650703"


@patch("src.utils_csv_excel.pd.read_excel")
def test_read_excel_file(mock_read_excel):
    df = pd.DataFrame({"id": ["650703", "593027"], "state": ["EXECUTED", "CANCELED"]})
    mock_read_excel.return_value = df
    result = read_excel_file("fake_excel_file.xlsx", state="CANCELED")
    assert result.iloc[0]["id"] == "593027"
