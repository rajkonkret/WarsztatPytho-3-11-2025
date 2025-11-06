from prototyp import Prototyp
from xyz import XYZ

# nie można utworzyc obiektu klasy abstrakcyjnej
# TypeError: Can't instantiate abstract class Prototyp
# without an implementation
# for abstract methods 'info', 'policz'
# pr = Prototyp(5)

xyz = XYZ(1, 2, 3)
print(xyz.info("xyz 001"))
# xyz 001xyz 001xyz 001
print(f"Policz: {xyz.policz()}")
# xyz 001xyz 001xyz 001
# Policz: 5
