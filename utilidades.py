import os
from os import system, name


def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


def menu():
    print('')
    print('\033[42m-=-\033[m'*13)
    print(
        '|\033[32m           Bem Vindo(a)!             \033[m|\n|\033[1;32m          JOGO do CHUTE!\033[m             |')
    print('| Vou pensar um número entre 1 a 100. |')
    print('|    Tente descobrir esse número.     |\033[m')
    print('\033[42m-=-\033[m'*13)
    print('')
