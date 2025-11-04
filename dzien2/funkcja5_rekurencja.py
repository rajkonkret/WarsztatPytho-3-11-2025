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
