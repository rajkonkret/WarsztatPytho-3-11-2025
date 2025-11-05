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
# <class '__main__.DefaultDict'>
# {}
# Default
