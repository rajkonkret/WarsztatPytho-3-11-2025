from prototyp import Prototyp
from xyz import XYZ
from regular import Regular

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

rg = Regular(4, 5)
print(rg.info("rg 002"))  # Wiadomość: rg 002
print(f"Policz: {rg.policz()}")
# Wiadomość: rg 002
# Policz: 3.2

rg.msg()
xyz.msg()
# Metoda nieabstrakcyjna klasy abstrakcyjnej
# Metoda nieabstrakcyjna klasy abstrakcyjnej

lista = [rg, xyz]  # obiekty róznych klas
# polimorfizm
# możemy potraktowac jako obiekt tej samej klasy abstrakcyjnej
for i in lista:
    print(i.policz())
# 3.2
# 5
