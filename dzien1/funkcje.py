# funkcja - fragment kodu, który można wykonac w dowolnym momencie
# funkcja musi zostac najpierw zadeklarowana
# wywołanie uruchamia kod
from typing import Tuple


# deklarcja funkcji
def odejmij():
    print(10 - 4)


# wywołaniae funkcji
odejmij()


def odejmij(a, b, c):
    print(a - b - c)


odejmij(4, 5, 6)  # -7


# argumenty o wartościach domyślnych pozwalają
# zasymolowac przeciażanie funkcji za pomocą liczby argumentów
def odejmij(a=0, b=0, c=0):
    print(a - b - c)


odejmij()

# pozycyjne
odejmij(1, 2)  # -1
odejmij(1, 2, 3)  # -4

# po nazwie
odejmij(c=90)  # -90
odejmij(b=90, a=85, c=90)  # -90

# mieszane
# odejmij(a=10, 2, 3) # SyntaxError: positional argument follows keyword argument
# pozycyjne przed nazwanymi
odejmij(10, 2, c=3)  # 5
odejmij(10, c=89)  # -79

# TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
# print(odejmij() + odejmij(10, 7))
print(odejmij())  # None, funkcja konczy się print(), nic nie zwraca


# funkcje zwracające wynik
def mnozenie(a, b):
    return a * b  # zwraca wynik


print(mnozenie(5, 6))  # 30
zmienna = mnozenie(7, 56)
print("Zmienna:", zmienna)  # Zmienna: 392


# tylko podpowiedzi
def mnozenie2(a: int, b: int) -> Tuple[int, int, int]:
    return a, b, a * b


# mnozenie2("q","2")
# TypeError: can't multiply sequence by non-int of type 'str'
print(2 * "Radek")  # RadekRadek
print("2" + "Radek")  # 2Radek, konkatenacja
# print("2" + 4)
# silne typownie - nie zmaienia typów podczas operacji
# TypeError: can only concatenate str (not "int") to str
a: int = "Radek"
print(a)
print(type(a))  # <class 'str'>

print(mnozenie2(2, 4))  # (2, 4, 8)
c = mnozenie2(2, 8)
# _ * _ = _
print(f"{c[0]} * {c[1]} = {c[2]}")  # 2 * 8 = 16
# (2, 4, 8)
a, b, wynik = mnozenie2(7, 9)
print(f"{a} * {b} = {wynik}")  # 7 * 9 = 63

print(mnozenie2("radek", 10))
# ('radek', 10, 'radekradekradekradekradekradekradekradekradekradek')
print(10 * "35")  # 35353535353535353535

# narzedzie skanowania kodu
# mypy
#  pip install mypy
# cd .\dzien1\
# (.venv) PS C:\Users\CSComarch\PycharmProjects\WarsztatPytho-3-11-2025> pip install mypy
# Collecting mypy
#   Downloading mypy-1.18.2-cp313-cp313-win_amd64.whl.metadata (2.2 kB)
# Collecting typing_extensions>=4.6.0 (from mypy)
#   Downloading typing_extensions-4.15.0-py3-none-any.whl.metadata (3.3 kB)
# Collecting mypy_extensions>=1.0.0 (from mypy)
#   Downloading pathspec-0.12.1-py3-none-any.whl.metadata (21 kB)
# Downloading mypy-1.18.2-cp313-cp313-win_amd64.whl (9.8 MB)
#    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 9.8/9.8 MB 50.5 MB/s eta 0:00:00
# Downloading mypy_extensions-1.1.0-py3-none-any.whl (5.0 kB)
# Downloading pathspec-0.12.1-py3-none-any.whl (31 kB)
# Downloading typing_extensions-4.15.0-py3-none-any.whl (44 kB)
# Installing collected packages: typing_extensions, pathspec, mypy_extensions, mypy
# Successfully installed mypy-1.18.2 mypy_extensions-1.1.0 pathspec-0.12.1 typing_extensions-4.15.0
#
# [notice] A new release of pip is available: 25.0.1 -> 25.3
# [notice] To update, run: python.exe -m pip install --upgrade pip
# (.venv) PS C:\Users\CSComarch\PycharmProjects\WarsztatPytho-3-11-2025> cd .\dzien1\
# (.venv) PS C:\Users\CSComarch\PycharmProjects\WarsztatPytho-3-11-2025\dzien1> mypy .\funkcje.py
# funkcje.py:6: note: "odejmij" defined here
# funkcje.py:14: error: Name "odejmij" already defined on line 6  [no-redef]
# funkcje.py:18: error: Too many arguments for "odejmij"  [call-arg]
# funkcje.py:23: error: Name "odejmij" already defined on line 6  [no-redef]
# funkcje.py:30: error: Too many arguments for "odejmij"  [call-arg]
# funkcje.py:31: error: Too many arguments for "odejmij"  [call-arg]
# funkcje.py:34: error: Unexpected keyword argument "c" for "odejmij"  [call-arg]
# funkcje.py:35: error: Unexpected keyword argument "b" for "odejmij"  [call-arg]
# funkcje.py:35: error: Unexpected keyword argument "a" for "odejmij"  [call-arg]
# funkcje.py:35: error: Unexpected keyword argument "c" for "odejmij"  [call-arg]
# funkcje.py:40: error: Too many arguments for "odejmij"  [call-arg]
# funkcje.py:40: error: Unexpected keyword argument "c" for "odejmij"  [call-arg]
# funkcje.py:41: error: Too many arguments for "odejmij"  [call-arg]
# funkcje.py:41: error: Unexpected keyword argument "c" for "odejmij"  [call-arg]
# funkcje.py:59: error: Syntax error in type annotation  [syntax]
# funkcje.py:59: note: Suggestion: Use Tuple[T1, ..., Tn] instead of (T1, ..., Tn)
# funkcje.py:70: error: Incompatible types in assignment (expression has type "str", variable has type "int")  [assignment]
# funkcje.py:82: error: Argument 1 to "mnozenie2" has incompatible type "str"; expected "int"  [arg-type]
# Found 16 errors in 1 file (checked 1 source file)
# (.venv) PS C:\Users\CSComarch\PycharmProjects\WarsztatPytho-3-11-2025\dzien1>

# rzutowanie
print(int("2") + int("4"))  # 6
print("2" + "4")  # 24
