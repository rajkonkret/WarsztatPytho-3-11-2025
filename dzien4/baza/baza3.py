# ORM to skrót od dwóch różnych terminów: w programowaniu to Object-Relational Mapping (mapowanie obiektowo-relacyjne),
# które jest techniką łączącą obiekty programistyczne z relacyjnymi bazami danych

# pip install sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

# echo=True - logowanie zdarzeń bazy danych
engine = create_engine('sqlite:///moja_baza.db', echo=True)
Base = declarative_base()


# # model, encja - klasa odwzorowująca tabele w bazie danych
class Person(Base):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(String)

    def __repr__(self):
        return f"{self.name}"


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
sesion = Session()

person = Person(name="Radek", age="23")
sesion.add(person)
sesion.commit()
# INSERT INTO person (name, age) VALUES (?, ?)

persons = sesion.query(Person).all()
print(persons)
# [Radek, Radek]
# SELECT person.id AS person_id, person.name AS person_name, person.age AS person_age
for p in persons:
    print(p.name)
# Radek
# Radek
