from functools import reduce

transactions = [
    {"id": 1, "type": "income", "amount": 1000, "currency": "USD"},
    {"id": 2, "type": "expense", "amount": 200, "currency": "USD"},
    {"id": 3, "type": "income", "amount": 500, "currency": "USD"},
    {"id": 4, "type": "expense", "amount": 300, "currency": "USD"},
    {"id": 5, "type": "income", "amount": 700, "currency": "USD"},
    {"id": 6, "type": "expense", "amount": 400, "currency": "EUR"},
    {"id": 7, "type": "income", "amount": 100, "currency": "EUR"},
]


# wyciągnięcie typu
# przemapowanie -> jesli ealuta inna niz zadana -> wstaw kwote 0 -> lista
# zsumujemy tak przygotane transakcje -> reduce

# raport

def filter_transactions(transactions, transoction_type):
    # pass
    return list(filter(lambda x: x['type'] == transoction_type, transactions))


def map_transactions(transactions, currency):
    # pass
    # operator warunkowy
    return list(map(lambda x: x['amount'] if x["currency"] == currency else 0, transactions))


def reduce_transactions(mapped):
    # pass
    return reduce(lambda x, y: x + y, mapped, 0)


def process_transactions(transactions, transoction_type, currency):
    filtered = filter_transactions(transactions, transoction_type)
    mapped = map_transactions(filtered, currency)
    total = reduce_transactions(mapped)

    return total


# def test_transaction_processing():
#     assert map_transactions(filter_transactions(transactions, "income"), "USD") == [1000, 500, 700, 0]


if __name__ == '__main__':
    print(process_transactions(transactions, "expense", "EUR"))  # 400

# pip install pytest
# Testing started at 08:23 ...
# Launching pytest with arguments C:\Users\CSComarch\PycharmProjects\WarsztatPytho-3-11-2025\dzien2\transakcje.py --no-header --no-summary -q in C:\Users\CSComarch\PycharmProjects\WarsztatPytho-3-11-2025\dzien2
#
# ============================= test session starts =============================
# collecting ... collected 1 item
#
# transakcje.py::test_transaction_processing PASSED                        [100%]
#
# ============================== 1 passed in 0.07s ==============================
#
# Process finished with exit code 0


# pytest .\transakcje.py
# pytest -v .\transakcje.py - bardziej szczegółowe
# (.venv) PS C:\Users\CSComarch\PycharmProjects\WarsztatPytho-3-11-2025\dzien2> pytest -v .\transakcje.py
# ==================================================================================================== test session starts ====================================================================================================
# platform win32 -- Python 3.13.9, pytest-8.4.2, pluggy-1.6.0 -- C:\Users\CSComarch\PycharmProjects\WarsztatPytho-3-11-2025\.venv\Scripts\python.exe
# cachedir: .pytest_cache
# rootdir: C:\Users\CSComarch\PycharmProjects\WarsztatPytho-3-11-2025\dzien2
# collected 1 item
#
# transakcje.py::test_transaction_processing PASSED                                                                                                                                                                      [100%]
#
# =



