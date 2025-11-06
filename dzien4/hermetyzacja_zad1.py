# hermetyzacja
class Boat:
    def __init__(self, model, year):
        self.model = model
        self.year = year
        # pole prywatne
        # widoczne tylko wewnątrz klasy
        self.__speed = 0

    def sail(self):
        self.__speed += 10
        self.__test()

    def speedometer(self):
        print(f"Speed is {self.__speed} knots.")

    def __test(self):
        print("All tested!")


boat = Boat("Omega", 2025)
boat.sail()
boat.sail()
boat.sail()
boat.sail()
boat.sail()
# AttributeError: 'Boat' object has no attribute '__speed'
# print(boat.__speed)  # 50
boat.speedometer()  # Speed is 50 knots.
boat.__speed = 0  # widocznośc publiczna
boat.__speed = 5  # pole o tej samej nazwie co prywatne w klasie ale inne pole
boat.speedometer()
# Speed is 50 knots.
# All tested!
# All tested!
# All tested!
# All tested!
# All tested!
# Speed is 50 knots.
# Speed is 50 knots.
# boat.__test()  # AttributeError: 'Boat' object has no attribute '__test'
# enkaspulacaj - hermetyzacja i wystawianie metod do zapisu i odczytu wartości pól
# settery, gettery
