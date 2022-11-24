from os import system
from meh import *

filename='Termékek.csv'
kosar='Kosár.csv'

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
    
    

  

 
