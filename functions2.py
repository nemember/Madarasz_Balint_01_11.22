from os import system
from meh import kosar , termekek

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

file=""


def Betoltes():
    file=open(filename, 'r', encoding='utf-8')
    for row in file:
        splitted=row.strip().split(';')
        termekek[splitted[0]]=int(splitted[1])
    file.close()


def Termekekkiirasa():
    system('cls')
    print('A termékék listája:\n ')
    sorsszam=1
    for key, value in termekek.items():
       print(f'{sorsszam} - {key} - {value}Ft')
       sorsszam+=1
    input('Tovább (Enter)')

def Kosarbarakas():
    system('cls')
    print('A termékék listája:\n ')
    sorsszam=1
    for key, value in termekek.items():
       print(f'{sorsszam} - {key} - {value}Ft')
       sorsszam+=1
    valasztas=int(input('Melyik terméket szeretné a kosárba helyezni (A sorszámát írja be)'))
    termekek_neve = list(termekek.keys())
    termekek_ara = list(termekek.values())
    kosar[termekek_neve[valasztas-1]] = termekek_ara[valasztas-1]
    input('Termék sikeresen kosárba rakva :)')
    





def Kosar():
    system('cls')
    print('A kosárban lévő termékek:\n ')
    sorsszam=1
    for key, value in kosar.items():
       print(f'{sorsszam} - {key} - {value}Ft')
       sorsszam+=1
    input('Tovább (Enter)')

  

 
