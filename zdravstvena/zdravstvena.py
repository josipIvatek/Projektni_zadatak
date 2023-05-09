class Zdravstvena:
    def __init__(self, oib, datum_izdavanja):
        self.__oib = oib
        self.__datum_izdavanja = datum_izdavanja

    @property
    def oib(self):
        return self.__oib

    @oib.setter
    def oib(self, oib):
        self.__oib = oib

    @property
    def datum_izdavanja(self):
        return self.__datum_izdavanja

    @datum_izdavanja.setter
    def datum_izdavanja(self, datum_izdavanja):
        self.__datum_izdavanja = datum_izdavanja

    def ispis(self):
        print('Informacije o zdravstvenoj iskaznici: ')
        print(f"\tOIB: {self.__oib}")
        print(f"\tDatum izdavanja: {self.__datum_izdavanja}")