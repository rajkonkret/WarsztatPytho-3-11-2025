# lambda - skrócony zapis funkcji
# lambda zwraca wynik
# funkcja anonimowa - możliwośc użycia funkcji w miejscu deklarcji


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
