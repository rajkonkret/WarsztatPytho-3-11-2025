# lambda - skrócony zapis funkcji
# lambda zwraca wynik
# funkcja anonimowa - możliwośc użycia funkcji w miejscu deklarcji


def liczymy(x, y):
    return x + y


print(liczymy(6, 9))  # 15

liczymy2 = lambda x, y: x + y  # lambda ma return
print(liczymy2(8, 90))  # 98

