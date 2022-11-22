from os import system

filename='Termékek.csv'

def menu():
    system('cls')
    print('-----MENÜ-----')
    print('0 - Bezárás')
    print('1 - Termékek')
    print('2 - Vásárlás')
    print('3 - Kosár')
    print('4 - Kosárból törlés')
    return input('Válsztás: ')