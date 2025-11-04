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
    time.sleep(1)
    print(f"Yield zwraca wartość: {i}")
