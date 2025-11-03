# lambda - skrócony zapis funkcji
# lambda zwraca wynik
# funkcja anonimowa - możliwośc użycia funkcji w miejscu deklarcji
from functools import reduce, lru_cache


def liczymy(x, y):
    return x + y


print(liczymy(6, 9))  # 15

liczymy2 = lambda x, y: x + y  # lambda ma return
print(liczymy2(8, 90))  # 98

# mapowanie danych
lista = [1, 2, 5, 56, 78, 89, 90, 100, 200, 500]

# zrobic listę z tymy wartościami do potęgi 2
lista_wyn = []  # pusta lista
for i in lista:
    lista_wyn.append(i ** 2)
print(lista_wyn)
# [1, 4, 25, 3136, 6084, 7921, 8100, 10000, 40000, 250000]

# list comprehensions
print([i ** 2 for i in lista])  # [1, 4, 25, 3136, 6084, 7921, 8100, 10000, 40000, 250000]


def zmien(x):
    return x ** 2


lista_wyn2 = []
for i in lista:
    lista_wyn2.append(zmien(i))

print(lista_wyn2)
# [1, 4, 25, 3136, 6084, 7921, 8100, 10000, 40000, 250000]

# funkcja wyższego rędu
# map() - na kolekcji wykonuje funkcje
print(f"Zastosowanie map(): {list(map(zmien, lista))}")
# Zastosowanie map(): [1, 4, 25, 3136, 6084, 7921, 8100, 10000, 40000, 250000]

# lambda jako funkcja anonimowa
# anonimowa - nie jest przypisana do żadnej nazwy(zmiennej)
print(f"Zastosowanie map(): {list(map(lambda z: z ** 2, lista))}")
# Zastosowanie map(): [1, 4, 25, 3136, 6084, 7921, 8100, 10000, 40000, 250000]
print(f"Zastosowanie map(): {list(map(lambda z: z ** 3, lista))}")
# Zastosowanie map(): [1, 8, 125, 175616, 474552, 704969, 729000, 1000000, 8000000, 125000000]
print(f"Zastosowanie map(): {list(map(lambda z: z ** 4, lista))}")
# Zastosowanie map(): [1, 16, 625, 9834496, 37015056, 62742241, 65610000, 100000000, 1600000000, 62500000000]

# filtrowanie danych
for i in lista:
    if i < 10:
        print(i, end=" : ")  # 1 : 2 : 5 : , end= znak końca lini

print()  # ustawi znak ońca lini na \n

# filter() - filtrowanie danych
print(f'Użycie filter(): {list(filter(lambda x: x < 10, lista))}')
# Użycie filter(): [1, 2, 5]
print(f'Użycie filter(): {list(filter(lambda x: x > 100, lista))}')
print(f'Użycie filter(): {list(filter(lambda x: x < 200, lista))}')
print(f'Użycie filter(): {list(filter(lambda x: x > 2000, lista))}')
# Użycie filter(): [200, 500]
# Użycie filter(): [1, 2, 5, 56, 78, 89, 90, 100]
# Użycie filter(): []
print(f"Użycie filter(): {list(filter(lambda x: x > 30 and x < 100, lista))}")  # Użycie filter(): [56, 78, 89, 90]
print(f"Użycie filter(): {list(filter(lambda x: 30 < x < 100, lista))}")  # Użycie filter(): [56, 78, 89, 90]

r0 = {'miasto': "Kielce"}
r1 = {"miasto": "Kielce", "ZIP": "25-900"}

print(r0['miasto'])
print(r1['miasto'])
# Kielce
# Kielce
print(r1['ZIP'])  # 25-900
# print(r0['ZIP'])  # KeyError: 'ZIP'

d_zip = lambda row: row.setdefault("ZIP", "00-000")
print(d_zip(r0))
print(d_zip(r1))
# 00-000
# 25-900
print(r0)
print(r1)
# {'miasto': 'Kielce', 'ZIP': '00-000'}
# {'miasto': 'Kielce', 'ZIP': '25-900'}

lata = [(2000, 29.7), (2001, 33.12), (2010, 32.92)]
print(max(lata))  # (2010, 32.92)
print(min(lata))  # (2000, 29.7)

print(max(lata, key=lambda c: c[1]))  # (2001, 33.12)
print(max(map(lambda c: (c[1], c), lata)))  # (33.12, (2001, 33.12))

# 33.12
print(max(map(lambda c: c[1], lata)))  # 33.12
print(max(map(lambda c: (c[1], c[0]), lata)))  # (33.12, 2001)

a = 10


def funkcja_glob():
    a = 15  # zmienna o zasiegu lokalnym
    # nie zmienia wartości zmiennej globalnej o tej samej nazwie
    print(a)


funkcja_glob()  # 15
print(a)  # 10


def funkcja_glob2():
    global a  # użyj zmiennej globalnej
    a = 15
    print(a)


funkcja_glob2()  # 15
print(a)  # 15, a globalne zostało zmienione

# calculates ((((1 + 2) + 3) + 4) + 5).
liczby = [1, 2, 3, 4, 5]
wynik = reduce(lambda x, y: x + y, liczby)
print("Wynik reduce x + y:", wynik)  # Wynik reduce x + y: 15

liczby = [1, 2, 3, 4, 5]
wynik = reduce(lambda x, y: x * y, liczby)
print("Wynik reduce x * y:", wynik)  # Wynik reduce x * y: 120


@lru_cache(maxsize=1000)  # dekorator
def fib_cached(n):
    if n < 2:
        return n
    return fib_cached(n - 1) + fib_cached(n - 2)


print(fib_cached(10))  # 55
print(fib_cached.cache_info())  # CacheInfo(hits=8, misses=11, maxsize=1000, currsize=11)
print(fib_cached(10))
print(fib_cached.cache_info())  # CacheInfo(hits=9, misses=11, maxsize=1000, currsize=11)
print(fib_cached(15))  # 610
print(fib_cached.cache_info())  # CacheInfo(hits=15, misses=16, maxsize=1000, currsize=16)

fib_cached.cache_clear()  # CacheInfo(hits=0, misses=0, maxsize=1000, currsize=0)
print(fib_cached.cache_info())
