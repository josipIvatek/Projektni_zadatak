def unos_osobne(redni_broj):
    osobna = {}
    osobna['broj'] = int(input(f'Unesite broj {redni_broj}. osobne iskaznice: '))
    osobna['oib'] = int(input(f'Unesite OIB sa {redni_broj}. osobne iskaznice: '))
    osobna['prebivalište'] = input(f'Unesite prebivalište sa {redni_broj}. osobne iskaznice: ')
    return osobna
