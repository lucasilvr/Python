#Faça um programa que leia duas listas de inteiros, com 10 elementos cada.
#A seguir, calcule e imprima o lista-comum correspondente, isto é, uma lista
#de elementos cujos valores na primeira lista e estão na segunda.

# Da pra fazer de outra forma

def lerlista(lista):
    for i in range(10):
        num = int(input('Digite um numero: '))
        lista.append(num)
    return lista

def comum(listaA, listaB, listaComum):
    for elemento in listaA:
        if elemento in listaB:
            listaComum.append(elemento)
    return listaComum

listaA = []
print('Lista A')
listaA = lerlista(listaA)

listaB = []
print('Lista B')
listaB = lerlista(listaB)

listaComum = []
listaComum = comum(listaA, listaB, listaComum)
print('Lista comum: ', listaComum)

