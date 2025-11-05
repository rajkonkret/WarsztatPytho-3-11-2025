# paradygmaty programowania obiektowego
# dziedziczenie, hermetyzacja, polimorfizm, abstrakcja
from pprint import pprint


class ContactList(list['Contact']):

    def search(self, name):
        matching_contact = []
        for c in self:
            if name.casefold().strip() in c.name.casefold().strip():
                matching_contact.append(c)
        return matching_contact


class Contact:
    # all_contacts = []  # lista wspólna dla wszystkich obiektów klasy
    all_contacts = ContactList()  # lista wspólna dla wszystkich obiektów klasy

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    # __repr__
    def __repr__(self):  # repr nadpisuje str
        return f"{self.name} {self.email}"


# dziedziczenie
class Suplier(Contact):
    """
    Klasa dziedziczy po kalsie Contact
    """

    def order(self, order):
        print(f"{order} zamówiono od {self.name}")


class Friend(Suplier):
    """
    Klasa dzieddziczy po klasie Suplier
    """

    def __init__(self, name, email, phone="000000000"):
        super().__init__(name, email)  # super() - musimy wywołac metode __init__ z klasy nadrzędnej
        self.phone = phone

    def __repr__(self):
        # return f"{self.name} {self.email} +48{self.phone}"
        # !r - teksty będą w cudzysłowiach -> +48'768900877'
        return f"{self.name!r} {self.email!r} +48{self.phone!r}"


c1 = Contact("Adam", "admin@wp.pl")
print(c1)  # Adam admin@wp.pl
c2 = Contact("Radek", "radek@wp.pl")
c3 = Contact("Tomek", "tomek@wp.pl")
print(c1.all_contacts)  # [Adam admin@wp.pl, Radek radek@wp.pl, Tomek tomek@wp.pl]
print(Contact.all_contacts)  # [Adam admin@wp.pl, Radek radek@wp.pl, Tomek tomek@wp.pl]

sup1 = Suplier("Marek", "marek@wp.pl")
print(sup1)  # Marek marek@wp.pl
print(sup1.all_contacts)
# [Adam admin@wp.pl, Radek radek@wp.pl, Tomek tomek@wp.pl, Marek marek@wp.pl]
# c1.order() # AttributeError: 'Contact' object has no attribute 'order'
sup1.order("kawa")  # kawa zamówiono od Marek

print(Contact.all_contacts.search("Radek"))  # [Radek radek@wp.pl]
osoba = Contact.all_contacts.search("Radek")
print(osoba)
print(osoba[0].name)  # Radek
print(osoba[0].email)  # radek@wp.pl

f1 = Friend("Kasia", "kasia@onet.pl")
f2 = Friend("Kamil", "kamil@onet.pl")
print(f1, f2)
# Kasia kasia@onet.pl +48000000000 Kamil kamil@onet.pl +48000000000

print(Contact.all_contacts)
# [Adam admin@wp.pl, Radek radek@wp.pl, Tomek tomek@wp.pl, Marek marek@wp.pl,
# Kasia kasia@onet.pl +48000000000, Kamil kamil@onet.pl +48000000000]

print(Contact.all_contacts.search("Kasia"))  # [Kasia kasia@onet.pl +48000000000]

f3 = Friend("Aneta", "aneta@wp.pl", "768900877")
print(f3)  # Aneta aneta@wp.pl +48768900877

print(Contact.all_contacts)
# [Adam admin@wp.pl, Radek radek@wp.pl, Tomek tomek@wp.pl, Marek marek@wp.pl, Kasia kasia@onet.pl +48000000000,
# Kamil kamil@onet.pl +48000000000, Aneta aneta@wp.pl +48768900877]

pprint(Contact.all_contacts)
# [Adam admin@wp.pl,
#  Radek radek@wp.pl,
#  Tomek tomek@wp.pl,
#  Marek marek@wp.pl,
#  Kasia kasia@onet.pl +48000000000,
#  Kamil kamil@onet.pl +48000000000,
#  Aneta aneta@wp.pl +48768900877]

# kolejnosc rozwiązywania nazw metod(pól) dla obiektu
pprint(Friend.__mro__)
# (<class '__main__.Friend'>,
#  <class '__main__.Suplier'>,
#  <class '__main__.Contact'>,
#  <class 'object'>)
