# metody statyczne - nie potrzebują obiektu klasy
class Matematyka:

    # def dodaj(self, a, b):
    #     return a + b
    @staticmethod
    def dodaj(a, b):
        return a + b

    @staticmethod
    def odejmij(a, b):
        return a - b


# kalk = Matematyka()
# print(kalk.dodaj(5, 9))

print(Matematyka.dodaj(5, 90))  # 95
print(Matematyka.dodaj(67, 90))  # 157
print(Matematyka.odejmij(67, 90))  # -23
