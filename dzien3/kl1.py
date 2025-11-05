# klasy - element programowania obiektowego
# szablon, przepis, pieczątka, matryca
# zawiera cechy (zmiennee) i metody (funkcje)
# obiekt (instancja) klasy - zbudowany wg przepisu
# klasa musi być znajpierw zadekalrowana
# tworzenie obiektu uruchamia metode __init__

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

    def __str__(self):
        return f"{self.x, self.y}"


ob = MyFirstClass()
print(ob)  # <__main__.MyFirstClass object at 0x00000173F52C6F90>
# po uzyciu __str__ -> (0, 0)
print(MyFirstClass.__doc__)  # Klasa w Pythonie
print(ob.x)
print(ob.y)
