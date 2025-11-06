from prototyp import Prototyp


class Regular(Prototyp):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y

    def policz(self):
        return (self.x / self.y) * 4

    def info(self, msg):
        return f'Wiadomość: {msg}'
