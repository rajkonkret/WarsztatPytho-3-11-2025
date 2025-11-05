# klasy - element programowania obiektowego
# szablon, przepis, pieczątka, matryca
# zawiera cechy (zmiennee) i metody (funkcje)
# obiekt (instancja) klasy - zbudowany wg przepisu
# klasa musi być znajpierw zadekalrowana
# tworzenie obiektu uruchamia metode __init__
import math


# PascalCase, UpperCamelCase
class MyFirstClass:
    """
    Klasa w Pythonie
    """

    def __init__(self, x=0, y=0):
        """
        Metoda inicjalizująca (konstruktor)
        :param x:
        :param y:
        """
        # self - obiekt
        self.x = x
        self.y = y

    def move(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def reset(self):
        self.move(0, 0)

    def calculate(self, other: "MyFirstClass") -> float:
        """
         For a two dimensional point (x, y), gives the hypotenuse
        using the Pythagorean theorem:  sqrt(x*x + y*y).
        :param other:
        :return:
        """
        return math.hypot(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f"{self.x, self.y}"


ob = MyFirstClass()
print(ob)  # <__main__.MyFirstClass object at 0x00000173F52C6F90>
# po uzyciu __str__ -> (0, 0)
print(MyFirstClass.__doc__)  # Klasa w Pythonie
print(ob.x)
print(ob.y)
# pydoc -b .\kl1.py - serwer z dokumentacją
#  pydoc -w kl1 - generuje html z dokumentacją

point1 = MyFirstClass(5, 9)
print(point1)  # (5, 9)

point1.move(56, 89)
print(point1)  # (56, 89)

point1.reset()
print(point1)  # (0, 0)

point2 = MyFirstClass(87, 90)
print(point2)  # (87, 90)

print(point2.calculate(point1))  # 125.1758762701504

point3 = MyFirstClass(43, 21)
point4 = MyFirstClass(13, 89)
print(point3)
print(point4)
# (43, 21)
# (13, 89)

print(point3.calculate(point2))
# 81.83520025025906

lista = [point1, point2, point3, point4]
print(lista)
# [<__main__.MyFirstClass object at 0x000002B313BB8E10>,
# <__main__.MyFirstClass object at 0x000002B313BB8F50>,
# <__main__.MyFirstClass object at 0x000002B31392A190>,
# <__main__.MyFirstClass object at 0x000002B313929E00>]