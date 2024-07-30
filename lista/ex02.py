'''Faça um programa que leia duas listas de inteiros, com 10 elementos cada.

# A seguir, calcule e imprima o lista-diferença correspondente, isto é, uma lista
# de elementos cujos valores na primeira lista e não estão na segunda.
'''
def lerlista(lista):
    lista = []
    for i in range(10):
       numero = int(input('Digite um numero: '))
       lista.append(numero)
    return lista

def diferente(listaA, listaB, listadif):
    for elemento in listaA:
        if elemento not in listaB:
            listadif.append(elemento)
    return listadif

listaA = []
listaB = []
listadif = []
print('Lista A')
listaA = lerlista(listaA)
print('\nLista B')
listaB = lerlista(listaB)
listadif = diferente(listaA, listaB, listadif)
print('Lista diferença: ', listadif)