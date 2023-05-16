from abc import ABC, abstractmethod

class Usluga(ABC):
    @abstractmethod
    def cijena_po_satu(self):
        pass
