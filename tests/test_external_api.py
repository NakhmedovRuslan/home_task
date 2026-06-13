from unittest.mock import Mock, patch

from src.external_api import transaction_convert


def test_transaction_convert_rub():
    data = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }
    assert transaction_convert(data) == 31957.58


@patch("src.external_api.API_KEY", "api_key")
@patch("src.external_api.requests.get")
def test_transaction_convert_usd(mock_get):
    data = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    }
    mock_response = Mock()
    mock_response.json.return_value = {"result": 610354.56635}
    mock_get.return_value = mock_response
    result = transaction_convert(data)
    assert result == 610354.56635
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert",
        headers={"apikey": "api_key"},
        params={
            "to": "RUB",
            "from": "USD",
            "amount": "8221.37",
        },
    )
