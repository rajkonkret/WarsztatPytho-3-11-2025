# napisz funkcje obliczająca średnią ocen
from openpyxl.workbook.views import BookView


def srednia_ocen(oceny):
    if not oceny:
        return 0
    return sum(oceny) / len(oceny)
# przykładowe użycie
oceny = [4, 5, 3, 4, 5]
print(f"Średnia ocen: {srednia_ocen(oceny)}")  # Średnia ocen: 4.2
oceny_puste = []
print(f"Średnia ocen (pusta lista): {srednia_ocen(oceny_puste)}")  # Średnia ocen (pusta lista): 0
# zrób refactoring tego kodu
def srednia_ocen_refaktoring(oceny):
    return sum(oceny) / len(oceny) if oceny else 0
# przykładowe użycie
print(f"Średnia ocen (refaktoring): {srednia_ocen_refaktoring(oceny)}")  # Średnia ocen (refaktoring): 4.2
print(f"Średnia ocen (pusta lista, refaktoring): {

srednia_ocen_refaktoring(oceny_puste)}")  # Średnia ocen (pusta lista, refaktoring): 0

# dopisz klase Book
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', year={self.year})"

# przykładowe użycie
book1 = Book("1984", "George Orwell", 1949)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
print(book1)  # Book(title='1984', author='George Orwell', year=1949)
print(book2)  # Book(title='To Kill a Mockingbird', author='Harper Lee', year=1960)
# napisz klase car
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __repr__(self):
        return f"Car(make='{self.make}', model='{self.model}', year={self.year})"
# przykładowe użycie
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2019)
print(car1)  # Car(make='Toyota', model='Camry', year=2020)
print(car2)  # Car(make='Honda', model='Civic', year=2019)

# napisz sqlite z sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# konfiguracja bazy danych
engine = create_engine('sqlite:///cars.db', echo=True)
Base = declarative_base()
# definicja modelu Car
class CarModel(Base):
    __tablename__ = 'cars'
    id = Column(Integer, primary_key=True)
    make = Column(String)
    model = Column(String)
    year = Column(Integer)
    def __repr__(self):
        return f"CarModel(id={self.id}, make='{self.make}', model='{self.model}', year={self.year})"
# tworzenie tabeli
Base.metadata.create_all(engine)
# tworzenie sesji
Session = sessionmaker(bind=engine)
session = Session()
# dodawanie przykładowych danych
car1 = CarModel(make="Toyota", model="Camry", year=2020)
car2 = CarModel(make="Honda", model="Civic", year=2019)
session.add(car1)
session.add(car2)
session.commit()
# zapytanie o wszystkie samochody
cars = session.query(CarModel).all()
for car in cars:
    print(car)
# zamknięcie sesji
session.close()
# zrob to w sqlalchemy 2.0 style
from sqlalchemy import create_engine, Column, Integer, String, select
from sqlalchemy.orm import declarative_base, Session
# konfiguracja bazy danych
engine = create_engine('sqlite:///cars_v2.db', echo=True)
Base = declarative_base()
# definicja modelu Car
class CarModelV2(Base):
    __tablename__ = 'cars_v2'
    id = Column(Integer, primary_key=True)
    make = Column(String)
    model = Column(String)
    year = Column(Integer)
    def __repr__(self):
        return f"CarModelV2(id={self.id}, make='{self.make}', model='{self.model}', year={self.year})"
# tworzenie tabeli
Base.metadata.create_all(engine)
# tworzenie sesji i dodawanie danych
with Session(engine) as session:
    car1 = CarModelV2(make="Ford", model="Focus", year=2018)
    car2 = CarModelV2(make="Chevrolet", model="Malibu", year=2021)
    session.add_all([car1, car2])
    session.commit()
    # zapytanie o wszystkie samochody
    stmt = select(CarModelV2)
    for car in session.scalars(stmt):
        print(car)