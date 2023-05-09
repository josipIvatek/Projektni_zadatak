from utilities import unos_telefona, unos_datuma
from .korisnik import Korisnik
from zdravstvena import Zdravstvena

def unos_korisnika(redni_broj):
    ime = input(f'Unesite ime {redni_broj}. korisnika: ').capitalize()
    prezime = input(f'Unesite prezime {redni_broj}. korisnika: ').capitalize()
    email = input(f'Unesite email {redni_broj}. korisnika: ').strip()
    telefon = unos_telefona(f'Unesite telefon {redni_broj}. korisnika: ')
    oib = input('Uneiste oib: ')
    datum_izdavanja = unos_datuma('Unesite dan isteka zdravtsvene iskaznice: ')


    return Korisnik(ime, prezime, email, telefon, Zdravstvena(oib, datum_izdavanja))