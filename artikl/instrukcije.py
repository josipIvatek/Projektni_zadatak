from .usluga import Usluga
from .artikl import Artikl

class Instrukcije(Artikl, Usluga):
    def __init__(self, naslov, opis, cijena):
        super().__init__(naslov,opis, cijena)

    def cijena_po_satu(self):
        cijena_po_satu = self._cijena/30
        return cijena_po_satu

    def ispis(self):
        print('Informacije o instrukcijama:')
        print(f'\tNaslov: {self.naslov}')
        print(f'\tOpis: {self.opis}')
        print(f'\tCijena po satu: {self.cijena_po_satu()}')

