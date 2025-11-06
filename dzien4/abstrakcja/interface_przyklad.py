from abc import ABC, abstractmethod


# zamiennik interfejsu
class Interface(ABC):

    @abstractmethod
    def policz(self):
        pass
