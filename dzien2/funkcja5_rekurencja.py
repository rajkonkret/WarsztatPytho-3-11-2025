# funkcja rekurencyjna
# wywołuje sama siebie

def silnia(n):
    if n == 0:
        return 1
    else:
        return n * silnia(n - 1)


print(silnia(5))  # 120


def nwd(a, b):
    if b == 0:
        return a
    return nwd(b, a % b)  # % modulo, reszta z dzielenia


print(nwd(48, 18))  # 6

nested_data = {
    "a": 1,
    "b": {
        "c": 2,
        "d": [3, 4, {"e": 5}]
    },
    "f": [6, 7]
}


# zsumowanie wszystkie wartości z tego słownika

def sum_nested(data):
    total = 0
    if isinstance(data, dict):
        for key, value in data.items():
            total += sum_nested(value)
    elif isinstance(data, list):
        for item in data:
            total += sum_nested(item)
    elif isinstance(data, (int, float)):
        total += data

    return total


result = sum_nested(nested_data)
print('Sum nested is:', result)  # Sum nested is: 28
