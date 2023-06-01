from .korisnik import Korisnik

class PrivatniKorisnik(Korisnik):

    def __init__(self, ime, prezime, email, telefon, drzavljanstvo):
        super().__init__(email, telefon)
        self.__ime = ime
        self.__prezime = prezime
        self.drzavljanstvo = drzavljanstvo

    @property
    def ime(self):
        return self.__ime

    @ime.setter
    def ime(self, ime):
        self.__ime = ime

    @property
    def prezime(self):
        return self.__prezime

    @prezime.setter
    def prezime(self, prezime):
        self.__prezime = prezime

    @property
    def drzavljanstvo(self):
        return self.drzavljanstvo

    @drzavljanstvo.setter
    def drzavljanstvo(self, drzavljanstvo):
        self.drzavljanstvo = drzavljanstvo

    def ispis(self):
      print("Informacije o privatnom korisniku: ")
      print(f'\tIme: {self.__ime}')
      print(f'\tPrezime: {self.__prezime}')
      print(f'\tTelefon: {self.telefon}')
      print(f'\tEmail: {self.email}')
      print(f'\tDrzavljanstvo: {self.drzavljanstvo}')
