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
print(a1['name'])
# {}
# name
print(a1)  # {'name': 0}


