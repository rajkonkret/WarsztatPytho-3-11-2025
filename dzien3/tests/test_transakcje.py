import pytest

import transakcje as tr

# assert - asrecja
x = 5


# assert x == 5
# assert x == 10

def test_filter_transactions_income():
    expected_list = [
        {"id": 1, "type": "income", "amount": 1000, "currency": "USD"},
        {"id": 3, "type": "income", "amount": 500, "currency": "USD"},
        {"id": 5, "type": "income", "amount": 700, "currency": "USD"},
        {"id": 7, "type": "income", "amount": 100, "currency": "EUR"},
    ]
    assert tr.filter_transactions(tr.transactions, "income") == expected_list


# map transactions
def test_map_transactions_usd():
    result = [1000, 200, 500, 300, 700, 0, 0]
    assert tr.map_transactions(tr.transactions, "USD") == result


# (.venv) PS C:\Users\CSComarch\PycharmProjects\WarsztatPytho-3-11-2025\dzien3> pytest -v .\tests\test_transakcje.py
# ==================================================================================================== test session starts ====================================================================================================
# platform win32 -- Python 3.13.9, pytest-8.4.2, pluggy-1.6.0 -- C:\Users\CSComarch\PycharmProjects\WarsztatPytho-3-11-2025\.venv\Scripts\python.exe
# cachedir: .pytest_cache
# rootdir: C:\Users\CSComarch\PycharmProjects\WarsztatPytho-3-11-2025\dzien3
# collected 2 items
#
# tests/test_transakcje.py::test_filter_transactions_income PASSED                                                                                                                                                       [ 50%]
# tests/test_transakcje.py::test_map_transactions_usd PASSED                                                                                                                                                             [100%]
#
# ===================================================================================================== 2 passed in 0.01s =====================================================================================================
# (.venv) PS C:\Users\CSComarch\PycharmProjects\WarsztatPytho-3-11-2025\dzien3>

# reduce
def test_reduce_transactions():
    assert tr.reduce_transactions([1000, 500, 700, 0]) == 2200


# ==================================================================================================== test session starts ====================================================================================================
# platform win32 -- Python 3.13.9, pytest-8.4.2, pluggy-1.6.0 -- C:\Users\CSComarch\PycharmProjects\WarsztatPytho-3-11-2025\.venv\Scripts\python.exe
# cachedir: .pytest_cache
# rootdir: C:\Users\CSComarch\PycharmProjects\WarsztatPytho-3-11-2025\dzien3
# collected 3 items
#
# tests/test_transakcje.py::test_filter_transactions_income PASSED                                                                                                                                                       [ 33%]
# tests/test_transakcje.py::test_map_transactions_usd PASSED                                                                                                                                                             [ 66%]
# tests/test_transakcje.py::test_reduce_transactions PASSED                                                                                                                                                              [100%]
#
# ===================================================================================================== 3 passed in 0.01s =====================================================================================================
# (.venv) PS C:\Users\CSComarch\PycharmProjects\WarsztatPytho-3-11-2025\dzien3>
def test_transaction_processing():
    assert tr.map_transactions(tr.filter_transactions(tr.transactions, "income"), "USD") == [1000, 500, 700, 0]


# tests/test_transakcje.py::test_filter_transactions_income PASSED                                                                                                                                                       [ 25%]
# tests/test_transakcje.py::test_map_transactions_usd PASSED                                                                                                                                                             [ 50%]
# tests/test_transakcje.py::test_reduce_transactions PASSED                                                                                                                                                              [ 75%]
# tests/test_transakcje.py::test_transaction_processing PASSED

# celowo błedny test
def test_map_transactions_usd_wrong():
    wrong = [1, 2, 3]
    assert tr.map_transactions(tr.transactions, "USD") == wrong


# ========================================================================================================= FAILURES ==========================================================================================================
# ______________________________________________________________________________________________ test_map_transactions_usd_wrong ______________________________________________________________________________________________
#
#     def test_map_transactions_usd_wrong():
#         wrong = [1, 2, 3]
# >       assert tr.map_transactions(tr.transactions, "USD") == wrong
# E       AssertionError: assert [1000, 200, 5..., 700, 0, ...] == [1, 2, 3]
# E
# E         At index 0 diff: 1000 != 1
# E         Left contains 4 more items, first extra item: 300
# E
# E         Full diff:
# E           [
# E         -     1,...
# E
# E         ...Full output truncated (13 lines hidden), use '-vv' to show
#
# tests\test_transakcje.py:67: AssertionError

# test parametryzowany dla process_transactions
@pytest.mark.parametrize(
    "kind,currency,expected",
    [
        ("income", "USD", 1000 + 500 + 700),
        ("income", "EUR", 100),
        ("expense", "USD", 200 + 300),
        ("expense", "EUR", 400),
    ]
)
def test_process_transactions_param(kind, currency, expected):
    assert tr.process_transactions(tr.transactions, kind, currency) == expected
