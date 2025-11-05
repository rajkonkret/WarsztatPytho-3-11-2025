class A:
    def method(self):
        print("Metoda z klasy A")


a = A()
a.method()  # Metoda z klasy A


class B:
    def method(self):
        print("Metoda z klasy B")


b = B()
b.method()  # Metoda z klasy B


# można dziedziczyc po wielu klasach
class C(B, A):
    """
    Klasa dziedziczy po klasie B i A
    """


c = C()
print(C.__mro__)  # (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
c.method()  # Metoda z klasy B


class D(A, B):
    """
    Klasa dziedziczy po A i B
    """


d = D()
d.method()  # Metoda z klasy A


class E(A, B):
    def method(self):
        print("Metoda z klasy E")


print(E.__mro__)
# (<class '__main__.E'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)

e = E()
e.method()  # Metoda z klasy E


class F(A, B):
    """
    Chcemy użyć method z klasy B
    """

    def method(self):
        B.method(self)  # jawnie wskazujemy z jakiej klasy użyc metody, przekuzujemy obiekt


f = F()
f.method()  # Metoda z klasy B


class G(A, B):
    def method(self):
        super().method()  # super() - możemy użyć super, tutaj klasa: A
        print('dopisane')
        B.method(self)


g = G()
g.method()  #


# problem dziedziczenia po wielu klasach
# kolejnośc dziedziczenia ma znaczenie
# Metoda z klasy A
# dopisane
# Metoda z klasy B
# class H(A, F):
#     def method(self):
#         super().method()  # super() - możemy użyć super, tutaj klasa: A
#         print('dopisane')
#         B.method(self)


# print(H.__mro__)  # TypeError: Cannot create a consistent method resolution order (MRO) for bases A, F
class H(F, A):
    def method(self):
        super().method()  # super() - możemy użyć super, tutaj klasa: A
        print('dopisane')
        B.method(self)


print(H.__mro__)
# (<class '__main__.H'>, <class '__main__.F'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
