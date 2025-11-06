# print(2 / 0)
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\WarsztatPytho-3-11-2025\dzien4\kl_wyjatki.py", line 1, in <module>
#     print(2 / 0)
#           ~~^~~
# ZeroDivisionError: division by zero

# raise ZeroDivisionError("Bład dzielenia")
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\WarsztatPytho-3-11-2025\dzien4\kl_wyjatki.py", line 8, in <module>
#     raise ZeroDivisionError("Bład dzielenia")
# ZeroDivisionError: Bład dzielenia
# print('Dalsza częśc programu')

class MyException(Exception):
    def __init__(self, message):
        super().__init__(message)


try:
    x = int(input("Podaj liczbę całakowitą większą od zera:"))
    if x <= 0:
        raise MyException("Liczba musi być większa od zera")
except MyException:
    print("Wartość musi byc większa od zera")
except ValueError as e:
    print("Bład wartości:", e)
except Exception as e:
    print("Bład:", e)
else:  # wykona się tylko wtedy gdy nie ma błedu
    print("Działanie na x:", x * 2)
finally:  # wykona się zawsze
    print("Koniec")

# Podaj liczbę całakowitą większą od zera:5
# Działanie na x: 10
# Koniec
