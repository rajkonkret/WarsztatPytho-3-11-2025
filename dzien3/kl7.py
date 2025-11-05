# Stworzyć system zarządzania biblioteką
# Book
# dodania ksiązek, wypozyczenia ksiązek, zwrot kisązki
# lista ksiązek do wypożyczenia, wypożyczonych
# title, author, isbn
# dodac klasę Library
# dekorator logujący zdarzenie, np .: udąlo sie wypożyczyc ksiazke
from datetime import datetime
from functools import wraps


def audit(action: str):
    """
    Dekorator dopisujący wpis do dziennika biblioteki
    """

    def deco(fn):
        @wraps(fn)
        def wrapper(self: "Library", *args, **kwargs):
            result = fn(self, *args, **kwargs)
            self._audit_log.append(
                f"{datetime.now():%Y-%m-%d %H:%M:%S} | {action} | {args=} {kwargs=}"
            )
            return result

        return wrapper

    return deco


class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __repr__(self):
        return f'Author: {self.author!r}, Tytuł: {self.title!r},  ISBN: {self.isbn!r}'


book = Book("Pan Tadeusz", "Adam Mickieicz", "1234567890")
print(book)  # Author: 'Adam Mickieicz', Tytuł: 'Pan Tadeusz',  ISBN: '1234567890'


class Library:
    def __init__(self):
        self._audit_log = []
        self.dostepne_ksiazki = []
        self.wypozyczone_ksiazki = []

    def fun_dostepne_ksiazki(self):
        return self.dostepne_ksiazki

    def fun_wypozyczone_ksiazki(self):
        return self.wypozyczone_ksiazki

    @audit("dodano ksiązkę")
    def fun_dodaj_ksiazke(self, book: "Book"):
        self.dostepne_ksiazki.append(book)

    @audit("zwrócono")
    def fun_wypozycz_ksiazke(self, isbn):
        for book in self.dostepne_ksiazki:
            if book.isbn == isbn:
                self.wypozyczone_ksiazki.append(book)
                self.dostepne_ksiazki.remove(book)
                return book
        raise Exception("Nie ma takiej ksiazki")

    def fun_zwroc_ksiazke(self, isbn):
        for book in self.wypozyczone_ksiazki:
            if book.isbn == isbn:
                self.wypozyczone_ksiazki.remove(book)
                self.dostepne_ksiazki.append(book)
                return book
        raise Exception("Ksiązka nie z naszej biblioteki")


biblioteka = Library()

while True:
    print(f"""
1. Dodaj książkę
2. Wypożycz ksiązkę
3. Pokaż dostępne
4. Pokaż wypozyczone
5. Zwróc ksiązkę
6. Koniec
""")

    try:
        odp = input("Wybierz oopcje:")  # zwaca str

        if odp == "1":
            author = input("Podaj autora:")
            title = input("Podaj tytuł:")
            isbn = input("Podaj numer ISBN:")
            biblioteka.fun_dodaj_ksiazke(Book(title, author, isbn))
        elif odp == "2":
            isbn = input("Podaj ISBN książki, ktorą chesz wypozyczyć:")
            book = biblioteka.fun_wypozycz_ksiazke(isbn)
            print(f"Książka zodstała wypożyczona: {book}")
        elif odp == "3":
            print(f'Dostępne ksiązki: {biblioteka.fun_dostepne_ksiazki()}')
        elif odp == "4":
            print(f'Wypożyczone ksiązki: {biblioteka.fun_wypozyczone_ksiazki()}')
        elif odp == "5":
            isbn = input("Podaj ISBN książki, ktorą chesz zwrócić:")
            book = biblioteka.fun_zwroc_ksiazke(isbn)
            if book:
                print(f"Książka zodstała zwrócona: {book}")
        elif odp == "6":
            break
        else:
            print("Błędny wybór")
        print(biblioteka._audit_log)
    except Exception as e:
        print("Błąd:", e)
