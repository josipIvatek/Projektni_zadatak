from datetime import date
from iznimke import IznimkaPrazanTekst, IznimkaTelefon

def unos_cijelog_pozitivnog_broja(poruka):
    while True:
        try:
            broj = int(input(poruka))

            if broj < 0:
                raise Exception('Morate upisati cijeli pozitivni broj!')

        except ValueError:
            print('Unesli ste znak a ne cijeli broj.')
        except Exception as e:
            print(e)
        else:
            return broj


def unos_realnog_pozitivnog_broja(poruka):
    while True:
        try:
            broj = float(input(poruka))

            if broj < 0:
                raise Exception('Morate upisati realni broj!')

        except ValueError:
            print('Unesli ste znak a ne realni broj.')
        except Exception as e:
            print(e)
        else:
            return broj


def unos_datuma(poruka):
    while True:
            try:
                dan = int(input(poruka))
                mjesec = int(input(f'Unesite mjesec isteka: '))
                godina = int(input(f'Unesite godinu isteka: '))
                datum = date(godina, mjesec, dan)

            except ValueError as e:
                print(e)
            else:
                return datum


def unos_intervala(min, max):
    while True:
        try:
            broj = int(input(f"Unesite cijeli broj u inervalu {min}-{max}: "))

            if broj<min or broj>max:
                raise Exception(f"Unesite broj unutar intervala {min}-{max}.")

        except ValueError:
            print('Unesli ste znak a ne cijeli broj.')
        except Exception as e:
            print(e)
        else:
            return broj

def unos_telefona(poruka):
    while True:
        try:
            broj = str(unos_cijelog_pozitivnog_broja(poruka))

            if len(broj) != 8:
                raise Exception(f"Broj telefona mora imati 8 znamenaka!")

        except Exception as e:
            print(e)
        else:
            return broj

def provjera_korisnickog_unosa(telefon, email, ime_ili_naziv, prezime_ili_web, drzavljanstvo_ili_web):
    while True:
        try:
            if len(telefon) == 0 or len(email) == 0 or len(ime_ili_naziv) == 0 or len(prezime_ili_web) == 0 or len(drzavljanstvo_ili_web) == 0:
                raise IznimkaPrazanTekst()
            elif len(str(telefon)) != 8:
                raise IznimkaTelefon()

            int(telefon)

        except IznimkaPrazanTekst as e:
            return str(e)

        except IznimkaTelefon as f:
            return str(f)

        except ValueError:
            return ('Telefon mora biti broj')

        else:
            return None
