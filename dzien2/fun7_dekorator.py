# dekorator - funkcja, przyjmuje inną funkcję jako argument
# dodaje, modyfikuje działanie tej funkcji (na wyniku tej funkcji)
# wykorzystuje mechanizm funkcji wewnętrznej


def dekor(func):
    def wew():
        print("Dekorator. Dodatkowy napis")
        return func()  # zwraca wynik funkcji

    return wew


