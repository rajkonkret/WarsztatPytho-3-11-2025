# zrobić dekorator, który zmienia wynik dziłania funkcji na duże litery

# funkcja -> zwraca tekst
# dekorator -> zamienia wynik na duże litery

def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)  # uruchamiamy funkcję
        return result.upper()

    return wrapper  # zwracamy adres, referencje


@uppercase_decorator
def greeting():
    return "Hello World!"


print(greeting())
# Hello World!
# po użyciu dekoratora: HELLO WORLD!

# teksty są nie mutowalne
tekst = "Radek"
# oryginał nie ulega zmianie
tekst.upper()
print(tekst)  # Radek
# """ Return a copy of the string converted to uppercase. """
# dostajemy kopię ze zmianami
print(tekst.upper())  # RADEK
wyn = tekst.upper()
print(wyn)  # RADEK


@uppercase_decorator
def greeting2(string):
    return f"Podałeś: {string}"


print(greeting2("Radek"))
# Podałeś: Radek
# dekorator -> PODAŁEŚ: RADEK
