# https://peps.python.org/pep-0008/
# snake_case
import sys

print()
print("Pierwsza linia")
print('Pierwsza linia')
# ctrl d  - powielanie linii
# ctrl / - komentarz w linii
# print('Pierwsza linia")
#   File "C:\Users\CSComarch\PycharmProjects\WarsztatPytho-3-11-2025\dzien1\wprowadzenie.py", line 8
#     print('Pierwsza linia")
#           ^
# SyntaxError: unterminated string literal (detected at line 8)
#
"""
Komentarz wielolinijkowy
dokumentacja
"""
info = """Tekst
wielolinijkow
    zachowuje
        formatowanie"""
print(info)
# Tekst
# wielolinijkow
#     zachowuje
#         formatowanie
print(info)
print(info)
print(info)
print(info)
print(info)

# typowaie dynamiczne - typ okreslany na podstawie zawartości
info = 90
print(info)
print(type(info))  # <class 'int'>, liczby całkowity
print(sys.int_info)
# sys.int_info(bits_per_digit=30,
# sizeof_digit=4,
# default_max_str_digits=4300,
# str_digits_check_threshold=640)

# kolekcje - może przechwywac dowlną ilość danych

# lista - zachowuje kolejność, moze przechowywac różne typy na raz
imiona = ["Jan", "Piotr", "Anna", "Nadia", "Michał"]
#           0       1        2        3       4
#           -5      -4       -3       -2       -1
print(imiona)
print(imiona[0])  # Jan, indeksowane od 0
# ctrl alt l - pomaga formatowac wg PEP8

# slicowanie - wyświetlenie fragmentu listy
print(imiona[2:4])  # ['Anna', 'Nadia'], od indeksy 2 do 3
print(imiona[1:])  # ['Piotr', 'Anna', 'Nadia', 'Michał'], włacznie z ostatnim
print(imiona[:4])  # ['Jan', 'Piotr', 'Anna', 'Nadia'] od indeksu 0 do końca

print(imiona[-1])  # ostatni eleement
print(imiona[-2:0])  # [] -> [3:0]
print(imiona[0:-2])  # ['Jan', 'Piotr', 'Anna']

imiona_parzyste = imiona[::2]  # ['Jan', 'Anna', 'Michał'] [start:stop:krok]
print(imiona_parzyste)

imiona.append("Karol")  # dodaje na koncu listy
print(imiona)  # ['Jan', 'Piotr', 'Anna', 'Nadia', 'Michał', 'Karol']
imiona.insert(1, "Leon")
print(imiona)  # ['Jan', 'Leon', 'Piotr', 'Anna', 'Nadia', 'Michał', 'Karol']

imiona.remove("Nadia")  # usunie pierwszy od lewej
print(imiona)  # ['Jan', 'Leon', 'Piotr', 'Anna', 'Michał', 'Karol']

del imiona[5]
print(imiona)  # ['Jan', 'Leon', 'Piotr', 'Anna', 'Michał']
print(imiona.pop(3))  # Anna, usunie po indeksie, zwraca usunięty element

# numeruje kolekcje
imen = enumerate(imiona, 111)
print(imen)
# for i in imen:
#     print(i)
#  (111, 'Jan')
# (112, 'Leon')
# (113, 'Piotr')
# (114, 'Michał')
#
# for i in imen:
#     print(i[0], i[1])
# 111 Jan
# 112 Leon
# 113 Piotr
# 114 Michał

# rospakowanie krotki
index, wartosc = (114, 'Michał')
# for index, wartosc in imen:
#     # f - string format
#     print(f"index -> {index}, wartość -> {wartosc}")
# index -> 111, wartość -> Jan
# index -> 112, wartość -> Leon
# index -> 113, wartość -> Piotr
# index -> 114, wartość -> Michał
print("index -> {}, wartość -> {}".format(index, wartosc))
print("index:", index, "wartość:", wartosc)  # index: 114 wartość: Michał
# sep
#         string inserted between values, default a space.
#       end
#         string appended after the last value, default a newline.
print("a: %i b: %s" % (index, wartosc))  # a: 114 b: Michał
# %s - str, %i - int
# sprawdza typy danych
# print("a: %i b: %i" % (index, wartosc))  # TypeError: %i format: a real number is required, not str

nowe_imie = imiona  # kopia referencji
pimie = imiona[:]
qimie = list(imiona)
lista_copy = imiona.copy()
print(nowe_imie)  # ['Jan', 'Leon', 'Piotr', 'Michał']
print(imiona)  # ['Jan', 'Leon', 'Piotr', 'Michał']
print(id(nowe_imie))  # 2313477006016
print(id(imiona))  # 2313477006016

print(id(pimie))  # 1277144576256
print(id(qimie))  # 1277146971776
print(id(lista_copy))  # 1277146925952

nowe_imie.append("Kunegunda")
print(nowe_imie)  # ['Jan', 'Leon', 'Piotr', 'Michał', 'Kunegunda']
print(imiona)  # ['Jan', 'Leon', 'Piotr', 'Michał', 'Kunegunda']
print(qimie)  # ['Jan', 'Leon', 'Piotr', 'Michał']

# krotka, tuple
# niemutowalna kolekcja
# miasto = 'Kraków', "Lublin", "Plock", "Łódź"
miasto = ('Kraków', "Lublin", "Plock", "Łódź")
print(type(miasto))  # <class 'tuple'>
print(miasto)  # ('Kraków', 'Lublin', 'Plock', 'Łódź')
# lepsze wykorzystanie pamieci

print(miasto.index("Łódź"))  # indeks 3
print(miasto.count("Łódź"))  # występuje 1 raz

# del miasto[0] # TypeError: 'tuple' object doesn't support item deletion
del miasto
# print(miasto)  # NameError: name 'miasto' is not defined
# garbage collector - odsmiecacz