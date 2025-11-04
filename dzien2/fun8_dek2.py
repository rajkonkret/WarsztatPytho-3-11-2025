# zrobić dekorator, który zmienia wynik dziłania funkcji na duże litery

# funkcja -> zwraca tekst
# dekorator -> zamienia wynik na duże litery

# pip install colorama
from colorama import Fore, Style, init
from functools import wraps

init(autoreset=True)


def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)  # uruchamiamy funkcję
        return result.upper()

    return wrapper  # zwracamy adres, referencje


# dekorator, który zmienia wynik na bold, czerwony
def bold_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return "\033[1m" + result + "\033[0m"

    return wrapper


def color_decorator(func):
    @wraps(func)  # przekazuje metadane do dekoratora
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return Fore.RED + result + Style.RESET_ALL

    return wrapper


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


@bold_decorator
@uppercase_decorator
def greeting2(string):
    return f"Podałeś: {string}"


print(greeting2("Radek"))


# Podałeś: Radek
# dekorator -> PODAŁEŚ: RADEK

@color_decorator
def greeting3(string):
    return f"Podałeś: {string}"


print(greeting3("Python"))
# Podałeś: Python

print(greeting3.__name__)  # wrapper
# po dodaniu @wraps() -> greeting3
# __name__
# __doc__
# __qualname__
