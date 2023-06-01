from artikl import get_artikl
from korisnik import get_korisnik
from kategorija import get_kategorija
from utilities import unos_datuma, unos_intervala
from .prodaja import Prodaja

def unos_prodaje(korisnici, kategorije, redni_broj):
    datum = unos_datuma('Unesite dan isteka prodaje: ')

    print(f'Odaberite korisnika {redni_broj}. prodaje')
    for i, korisnik in enumerate(korisnici, start=1):
        print(get_korisnik(i, korisnik))

    odabrani_korisnik = unos_intervala(1, len(korisnici))
    korisnik = korisnici[odabrani_korisnik - 1]

    print(f'Odaberite kategoriju {redni_broj}. prodaje')
    for i, kategorija in enumerate(kategorije, start=1):
        print(get_kategorija(i, kategorija))

    odabrana_kategorija = unos_intervala(1, len(kategorije))

    print(f'Odaberite artikl {redni_broj}. prodaje')
    for i, artikl in enumerate(kategorije[odabrana_kategorija - 1].artikli, start=1):
        print(get_artikl(i, artikl))

    odabrani_artikl = unos_intervala(1, len(kategorije[odabrana_kategorija - 1].artikli))
    artikl = kategorije[odabrana_kategorija - 1].artikli[odabrani_artikl - 1]
    return Prodaja(datum, korisnik, artikl)
