from abc import ABC, abstractmethod

class Palto(ABC):
    def __init__(self, V):
        self.V = V

    @abstractmethod
    def consumption(self):
        pass

class PaltoForWomen(Palto):
    def __init__(self, V):
        super().__init__(V)

    @property
    def consumption(self):
        return self.V/6.5 + 0.5

class Kostum(ABC):
    def __init__(self, H):
        self.H = H

    @abstractmethod
    def consumption(self):
        pass

class KostumForMen(Kostum):
    def __init__(self, H):
        super().__init__(H)

    @property
    def consumption(self):
        return 2 * self.H + 0.3


#не понял почему именно такие формулы, но менять не стал
palto = PaltoForWomen(58)
print(palto.consumption)

kostum = KostumForMen(190)
print(kostum.consumption)

