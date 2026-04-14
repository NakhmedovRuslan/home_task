from src.processing import filter_by_state, sort_by_date

def test_filter_by_state(transactions, transactions_executed, transactions_canceled):
    assert filter_by_state(transactions) == transactions_executed
    assert filter_by_state(transactions, state="CANCELED") == transactions_canceled


def test_sort_by_date(transactions, transactions_date):
    assert sort_by_date(transactions) == transactions_date