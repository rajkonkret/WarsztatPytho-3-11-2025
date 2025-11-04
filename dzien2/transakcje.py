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
    pass


def map_transactions(filtered, currency):
    pass


def reduce_transactions(mapped):
    pass


def process_transactions(transactions, transoction_type, currency):
    filtered = filter_transactions(transactions, transoction_type)
    mapped = map_transactions(filtered, currency)
    total = reduce_transactions(mapped)

    return total
