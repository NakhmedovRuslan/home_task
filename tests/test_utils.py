import json

from src.utils import operations


def test_operations_with_file(tmp_path):
    file = tmp_path / "testoperations.json"
    file.write_text(
        json.dumps(
            [
                {
                    "id": 441945886,
                    "state": "EXECUTED",
                    "date": "2019-08-26T10:50:58.294041",
                    "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод организации",
                    "from": "Maestro 1596837868705199",
                    "to": "Счет 64686473678894779589",
                }
            ]
        )
    )

    result = operations(file)
    assert result == [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        }
    ]


def test_operations_without_file():
    result = operations("fake_operations.json")
    assert result == []


def test_operations_with_broken_file(tmp_path):
    file = tmp_path / "broken_operations.json"
    file.write_text(json.dumps("{'hello'}"))
    result = operations(file)
    assert result == []
