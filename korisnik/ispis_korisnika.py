from kartica import ispis_kartice
def ispis_korisnika(korisnik):
    print('Informacije o korisniku: ')
    print(f"\tIme: {korisnik['ime']}")
    print(f"\tPrezime: {korisnik['prezime']}")
    print(f"\tTelefon: {korisnik['telefon']}")
    print(f"\tEmail: {korisnik['email']}")
    ispis_kartice(korisnik['kartica'])

def get_korisnik(redni_broj, korisnik):
    return f"{redni_broj}.  {korisnik['ime']} {korisnik['prezime']}"


