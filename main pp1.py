from datetime import date

korisnik = {}
korisnik['ime'] = input('Unesite ime korisnika: ').capitalize()
korisnik['prezime'] = input('Unesite prezime korisnika: ').capitalize()
korisnik['mail'] = input('Unesite email korisnika: ').strip()
korisnik['tel'] = int(input('Unesite telefon korisnika: '))

artikl={}
artikl['naslov'] = input('Unesite naslov artikla: ')
artikl['opis'] = input('Unesite opis artikla: ')
artikl['cijena'] = float(input('Unesite cijenu artikla: '))

prodaja = {}
dan = int(input('Unesite dan isteka prodaje: '))
mjesec = int(input('Unesite mjesec isteka prodaje: '))
godina = int(input('Unesite godinu isteka prodaje: '))
prodaja['datum'] = date(godina, mjesec, dan)
prodaja['korisnik'] = korisnik
prodaja['artikl'] = artikl

print('Informacije o artiklu: ')
print('\t Naslov:', prodaja['artikl']['naslov'])
print('\t Opis:', prodaja['artikl']['opis'])
print('\t Cijena:', prodaja['artikl']['cijena'])

print('Datum isteka prodaje: ')
print('\t Dan:', prodaja['datum'].day)
print('\t Mjesec:', prodaja['datum'].month)
print('\t Godina:', prodaja['datum'].year)

print('Informacije o korisniku: ')
print('\t', prodaja['korisnik']['ime'], prodaja['korisnik']['prezime'])
print('\t Telefon:', prodaja['korisnik']['tel'] )
print('\t Email:', prodaja['korisnik']['mail'])



