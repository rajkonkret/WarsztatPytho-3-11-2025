from prototyp import Prototyp


class XYZ(Prototyp):
    def __init__(self, x, a, b):
        super().__init__(x)
        self.a = a
        self.b = b

    def policz(self):
        return self.x * (self.a + self.b)

    def info(self, msg):
        return msg * 3
