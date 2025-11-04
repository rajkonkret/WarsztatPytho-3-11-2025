import time
from itertools import zip_longest


def wznowienie(n, k):
    print("Wstrzymanie działania...")
    yield 1001
    print("Wznowienie działania")
    yield n + k
    print("Działanie - dodawanie - Wstzrymanie")
    print("Wznowienie działania")
    n = 3 * n
    yield n - k
    print("Wznowienie działania - mnożenie")
    yield n * k
    print("Wznowienie działania - dzielenie")
    yield n / k


print(20 * "-")

print(wznowienie(6, 7))
print(list(wznowienie(6, 7)))

print(20 * "-")
for i in wznowienie(6, 8):
    if i == 1001:
        continue
    # time.sleep(1)
    print(f"Yield zwraca wartość: {i}")

print(20 * "-")


def gen4():
    i = 1
    while True:
        yield i * i
        i += 1


g4 = gen4()
print(next(g4))
print(next(g4))
print(next(g4))
print(next(g4))
print(next(g4))
print(next(g4))


def gen5():
    i = 1
    while True:
        command = yield i * i
        print(command)
        if command == "stop":
            break  # zatrzyma generator
        i += 1


g5 = gen5()
print(next(g5))
print(next(g5))
print(next(g5))
print(next(g5))

g5.send("OK")  # OK

try:
    g5.send("stop")  # StopIteration
except StopIteration:
    print("Koniec danych")
except Exception as e:
    print("Bład:", e)


# stop
# Koniec danych


def fibo_with_index(n):
    a, b = 0, 1
    for ind in range(n):
        yield ind, a
        a, b = b, a + b


fib = fibo_with_index(10)
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
# (0, 0)
# (1, 1)
# (2, 1)
# (3, 2)

for i, n in fibo_with_index(10):
    print(f"Pozycja: {i}, element: {n}")
# Pozycja: 0, element: 0
# Pozycja: 1, element: 1
# Pozycja: 2, element: 1
# Pozycja: 3, element: 2
# Pozycja: 4, element: 3
# Pozycja: 5, element: 5
# Pozycja: 6, element: 8
# Pozycja: 7, element: 13
# Pozycja: 8, element: 21
# Pozycja: 9, element: 34

person = ["Radek", "Tomek", "Zenek", "Ania", "Kasia"]
wiek = [34, 56, 57, 89]

for p, w in zip(person, wiek):
    print(p, w)
# Radek 34
# Tomek 56
# Zenek 57
# Ania 89

print(20 * "-")
zipped = zip_longest(person, wiek, fillvalue="Brak danych")
print(zipped)  # <itertools.zip_longest object at 0x000001AE8EED0400>

lista = list(zipped)  # wyczerpalismy dane z generatora
print(25 * "-")
for imie, wiek in zipped:
    print(imie, wiek)
# -------------------------
# Radek 34
# Tomek 56
# Zenek 57
# Ania 89
# Kasia Brak danych
print(25 * "-")
for imie, wiek in zipped:
    print(imie, wiek)
# dane wyczerpane
# -------------------------
for imie, wiek in lista:
    print(imie, wiek)
# -------------------------
# -------------------------
# Radek 34
# Tomek 56
# Zenek 57
# Ania 89
# Kasia Brak danych
