from kategorija import unos_kategorije
from korisnik import unos_korisnika
from prodaja import unos_prodaje, ispis_prodaje
from osobna import unos_osobne

korisnici = []
kategorije = []
prodaje = []
osobne = []

br_osobnih = int(input('Unesite broj osobnih iskaznica: '))
for i in range(1,br_osobnih+1):
    osobna = unos_osobne(i)
    osobne.append(osobna)

br_korisnika = int(input('Unesite broj korisnika: '))
for i in range(1,br_korisnika+1):
    korisnik = unos_korisnika(osobne, i)
    korisnici.append(korisnik)

br_kategorija = int(input('Unesite broj kategorija: '))
for i in range(1,br_kategorija+1):
    kategorija = unos_kategorije(i)
    kategorije.append(kategorija)

br_prodaja = int(input('Unesite broj prodaja: '))
for i in range(1,br_prodaja+1):
    prodaja = unos_prodaje(korisnici, kategorije, i)
    prodaje.append(prodaja)


for i,prodaja in enumerate(prodaje, start = 1):
    print(f"Prodaja {i}")
    ispis_prodaje(prodaja)


