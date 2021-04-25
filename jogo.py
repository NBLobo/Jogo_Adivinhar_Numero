# from random import randint
from time import sleep
from utilidades import menu, clear
from gerador_numero import gerador_de_numeros, gerar_lista


def pensarnumero():

    computador = gerar_lista()
    print('\033[4;31mPROCESSANDO!!!....\033[m')
    sleep(2)
    jogador = int(input('Em que número eu pensei? '))

    return jogador, computador


jogo = input('Está pronto para iniciar?(sim/não): ').lower().strip()[0]
if jogo != 's':
    print('\033[1;32mAté a próxima!!!...\n Fim do Jogo.\033[m')
    exit
else:
    print('OK! VAMOS AO JOGO.')
    clear()
    menu()
    jogador, computador = pensarnumero()
    sleep(1)


x = 0
while True:

    if 1 <= jogador <= 100:
        x += 1
        if jogador == computador:
            print(
                '\033[1;31;46mPARABÉNS!!!! Você venceu, com {} chutes.\033[m'.format(x))
            x = 0
            jogo = input('Vamos jogar mais uma?(s/n): ')
            if jogo == 's':
                clear()
                menu()
                print(
                    '\033[1;33m***************NOVO JOGO***************\033[m')
                jogador, computador = pensarnumero()
            else:
                print('\033[1;32mAté a próxima!!!...\n Fim do Jogo.\033[m')
                break
        elif jogador > computador:
            jogador = int(input('Digite um número menor {}: '.format(jogador)))
        elif jogador < computador:
            jogador = int(input('Digite um número maior {}: '.format(jogador)))
    else:
        print('Erro: Você deve digitar um número de 1 a 100! Tente novamente.')
        jogador, computador = pensarnumero()
else:
    clear()
    print('\033[1;32m ATÉ A PRÓXIMA!!!!\033[m\n \033[1;32mFim do Jogo!\033[m')
