import time


def wznowienie(n, k):
    print("Wstrzymanie działania...")
    yield 1001
    print("Wznowienie działania")
    yield n + k
    print("Działanie - dodawanie - Wstzrymanie")
    print("Wznowienie działania")
    n = 3 * n
    yield n - k
    print("Wznowienie działania - mnożenie")
    yield n * k
    print("Wznowienie działania - dzielenie")
    yield n / k


print(20 * "-")

print(wznowienie(6, 7))
print(list(wznowienie(6, 7)))

print(20 * "-")
for i in wznowienie(6, 8):
    if i == 1001:
        continue
    # time.sleep(1)
    print(f"Yield zwraca wartość: {i}")

print(20 * "-")


def gen4():
    i = 1
    while True:
        yield i * i
        i += 1


g4 = gen4()
print(next(g4))
print(next(g4))
print(next(g4))
print(next(g4))
print(next(g4))
print(next(g4))


def gen5():
    i = 1
    while True:
        command = yield i * i
        print(command)
        if command == "stop":
            break  # zatrzyma generator
        i += 1


g5 = gen5()
print(next(g5))
print(next(g5))
print(next(g5))
print(next(g5))

g5.send("OK")  # OK

try:
    g5.send("stop")  # StopIteration
except StopIteration:
    print("Koniec danych")
except Exception as e:
    print("Bład:", e)
# stop
# Koniec danych
