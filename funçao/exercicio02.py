'''
Rescreva o programa abaixo que procure em uma lista um valor fornecido e
retorne posição onde ele foi encontrado ou -1 caso não esteja na lista, mas
utilizando uma função.

lista = [1, 2, 10, 5, 20]
valor = 10
pos = -1
for i in range(len(lista)):
    if lista[i] == valor:
        pos = i
print(pos)
'''
#Função para retornar posição
def retornarPosicao(lista):
    valor = 10
    pos = -1
    for i in range(len(lista)):
        if lista[i] == valor:
            pos = i
    return pos

#Programa Principal
lista = [1, 2, 10, 5, 20]
pos = retornarPosicao(lista)
print(pos)