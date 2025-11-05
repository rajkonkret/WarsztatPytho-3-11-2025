# longest() - znajduje najdłuzszy klucz w słowniku
class LongestKeyDict(dict):
    def longest_key(self):
        longest = None
        for key in self:  # pętla standardowo zwraca klucze
            if longest is None or len(key) > len(longest):
                longest = key
        return longest


art = LongestKeyDict()
art['tomasz'] = 12
art['abraham'] = 8
art['zen'] = 2

print(art.longest_key())  # abraham


class LongestKeyDictMax(dict):
    def longest_key(self):
        return max(self.keys(), key=len, default=None)


art = LongestKeyDictMax()
art['tomasz'] = 12
art['abraham'] = 8
art['zen'] = 2

print(art.longest_key())  # abraham

assert "abraham" == art.longest_key()
# assert "zen" == art.longest_key()
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\WarsztatPytho-3-11-2025\dzien3\kl5.py", line 32, in <module>
#     assert "zen" == art.longest_key()
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^
# AssertionError
