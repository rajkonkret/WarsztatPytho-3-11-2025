# generator - generuje wartość w momencie kiedy jest potrzebna
import time


def kwadrat(n):
    for x in range(n):
        print(x ** 2)


kwadrat(5)


# generator
def kwadrat2(n):
    for x in range(n):
        yield x ** 2  # zwraca wartość oblicznia, pamięta który jest nastepny


kwa = kwadrat2(5)  # tworzymy generator
print(type(kwa))  # <class 'generator'>
print(kwa)  # <generator object kwadrat2 at 0x000001BD6751A8E0>

print(next(kwa))  # 0
print(next(kwa))  # 1
print(next(kwa))  # 4
print(next(kwa))  # 9

print("Zrób cokolwiek")
print("Kolejne zadania")

print(next(kwa))  # 16
# print(next(kwa))  # StopIteration - koniec danych w generatorze

kwa2 = kwadrat2(10)
for k in kwa2:
    print(k)
    print("Przetwarzam dane...")
    time.sleep(1)

# generatory niezależne od siebie
kwa3 = kwadrat2(10)
kwa4 = kwadrat2(10)

print(next(kwa3))  # 0
print(next(kwa3))  # 1
print(next(kwa3))  # 4

print(next(kwa4))  # 0
print(next(kwa4))  # 1

print(next(kwa3))  # 9
