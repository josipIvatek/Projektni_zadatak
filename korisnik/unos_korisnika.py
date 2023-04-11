from kartica import unos_kartice

def unos_korisnika(redni_broj):
    korisnik={}
    korisnik['ime'] = input(f'Unesite ime {redni_broj}. korisnika: ').capitalize()
    korisnik['prezime'] = input(f'Unesite prezime {redni_broj}. korisnika: ').capitalize()
    korisnik['telefon'] = int(input(f'Unesite telefon {redni_broj}. korisnika: '))
    korisnik['email'] = input(f'Unesite email {redni_broj}. korisnika: ').strip()
    korisnik['kartica'] = unos_kartice(redni_broj)

    return korisnik
