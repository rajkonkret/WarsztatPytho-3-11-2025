# słownik
# gdy klucz nie istnieje mamy:  KeyError
# __missing__ - wykonywana gdy nie ma klucza w słowniku

class DefaultDict(dict):
    def __missing__(self, key):
        return "Default"


d_python = {}
print(type(d_python))  # <class 'dict'>
# print(d_python['name'])  # KeyError: 'name'

d1 = DefaultDict()
print(type(d1))
print(d1)
print(d1['name'])


# <class '__main__.DefaultDict'>kur
# {}
# Default

# słownik w którym gdy nie ma klucza, tworzy taki klucz z wartością domyślną np.: 0
class AutoKeyDict(dict):
    def __missing__(self, key):
        self[key] = 0
        return key


a1 = AutoKeyDict()
print(a1)
# {}
print(a1['name'])
print(a1)  # {'name': 0}

a2 = AutoKeyDict()
a2["age"] = 34
print(a2)
# {}
print(a2['name'])
print(a2)  # {'name': 0}


# {'age': 34}
# name
# {'age': 34, 'name': 0}


# zmienia klucze na małe litery
class CaseInsensitiveDict(dict):
    def __missing__(self, key):
        # return self.get(key.lower())
        if isinstance(key, str):
            return self[key.lower()]
        return key


c1 = CaseInsensitiveDict()
c1['name'] = "Radek"
print(c1)  # {'name': 'Radek'}
print(c1['Name'])  # Radek
print(c1[1])  # 1
c1[1] = "tekst"
print(c1)  # {'name': 'Radek', 1: 'tekst'}
print(c1[1])  # tekst
