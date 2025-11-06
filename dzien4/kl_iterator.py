# iterator
# dane tylkogdy potrzebna

lista = [1, 2, 3, 4, 5]
iterator = iter(lista)
print(next(iterator))
print(next(iterator))
print(next(iterator))
# 1
# 2
# 3
print("Coś innego")
print(next(iterator))


# Coś innego
# 4

class Count:
    def __init__(self, lows, high):
        """
        metoda inicjalizująca
        :param lows:
        :param high:
        """
        self.current = lows
        self.highs = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.highs:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1


print(25 * "-")
counter = Count(1, 5)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
try:
    print(next(counter))
except StopIteration as e:
    print("Koniec:", e)
# Koniec:
