def unos_kartice(redni_broj):
    kartica={}
    kartica['iban'] = int(input(f'Unesite iban {redni_broj}. kartice: '))
    kartica['pin'] = int(input(f'Unesite pin {redni_broj}. kartice: '))
    kartica['k_broj'] = int(input(f'Unesite kratki broj {redni_broj}. kartice: '))
    return kartica

