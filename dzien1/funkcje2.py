# funkcja wewnętrzna, funjkcja zagnieżdzona
# dekorator - ma konstrukcje zbliżoną do funkcji wewnętrznej
# funkcje wyższego rzędu - przyjmuje lub zwraca inne funkcje
def fun1():
    print("To jest funkcja1")

    def fun2():
        print("To jest fun2")

    # fun2() - zwrócenie wartości
    # znamy adres fun2
    return fun2  # zwrócenie adresu fun2, referencje


fun1()
new_fun = fun1()
print(type(new_fun))  # <class 'function'>
print(new_fun)  # <function fun1.<locals>.fun2 at 0x0000012E3C283D80>
new_fun()
new_fun()
new_fun()


# To jest fun2
# To jest fun2
# To jest fun2

# zrobic funkcje plik
# funkcja przyjmuje parametr: zapis, odczyt
# w zależności od parametru zwróci funkcję odczyt, zapis
def plik(arg):
    def zapis():
        print("Zapisałem plik")

    def odczyt():
        print("Odczytałem plik")

    def pusta():
        print("Pusta")

    #
    match arg.casefold():
        case "zapis":
            return zapis  # zwracamy adres funkcji
        case "odczyt":
            return odczyt
        case _:
            return pusta

    # if arg.casefold() == "zapis":
    #     return zapis
    # else:
    #     return odczyt


zapis_pliku = plik("zapis")
zapis_pliku()
zapis_pliku()
zapis_pliku()
zapis_pliku()
zapis_pliku()

odczyt_pliku = plik("odczyty")
odczyt_pliku()

zapis_pliku()
odczyt_pliku()
# Zapisałem plik
# Zapisałem plik
# Zapisałem plik
# Zapisałem plik
# Zapisałem plik
# Pusta
# Zapisałem plik
# Pusta

# 'w'       open for writing, truncating the file first - jeśli plik istaniał, zostanie usunięty
fh = open("test.txt", "w")
fh.write("Zapisano\n")
fh.close()
