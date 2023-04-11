from osobna import get_osobna

def unos_korisnika(osobne, redni_broj):
    korisnik={}
    korisnik['ime'] = input(f'Unesite ime {redni_broj}. korisnika: ').capitalize()
    korisnik['prezime'] = input(f'Unesite prezime {redni_broj}. korisnika: ').capitalize()
    korisnik['telefon'] = int(input(f'Unesite telefon {redni_broj}. korisnika: '))
    korisnik['email'] = input(f'Unesite email {redni_broj}. korisnika: ').strip()

    print(f"Odaberite osobnu iskaznicu za {redni_broj}. korisnika.")
    for i, osobna in enumerate(osobne, start=1):
        print(get_osobna(i, osobna))

    odabrana_osobna = int(input('Odabrana osobna: '))
    korisnik['osobna'] = osobne[odabrana_osobna - 1]
    return korisnik
