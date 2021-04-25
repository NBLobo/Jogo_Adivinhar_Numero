import random
print('  Olá!!!!!!  ')

# Gerador de números


def gerador_de_numeros():
    i = 1
    while 1 <= i <= 100:
        yield i
        i += 1


# Cria a lista de numeros válidos
def gerar_lista():
    lista = [x for x in gerador_de_numeros()]
#    print(lista)
# Embaralhar os números da lista
#    random.shuffle(lista)
#    print(lista)
# Seleciona um número da lista
    for x in random.sample(lista, 1):
        return(x)
# gerar_lista()


# Definir uma faixa de números inteiros(int)
""" 
def faixa_int():
    while True:
        minimo = int(input('Digite o valor mínimo: '))
        maximo = int(input('Digite o valor máximo: '))
        if minimo < 1 or maximo > 100:
            print(
                f'Valor inválido. Digite um valor entre 1 e 100: ')
        else:
            return(minimo, maximo) 
minimo, maximo = faixa_int()
print(f'Minimo: {minimo}, Máximo: {maximo}') """
