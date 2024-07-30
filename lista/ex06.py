#Faça um programa em Python para ler, por meio de uma função, uma lista V
#de elementos inteiros. Escreva uma função para separar a lista V em duas
#listas A e B. A lista A deve conter os elementos positivos de V e a lista B os
#elementos negativos de V. Os elementos nulos de V não devem ser
#considerados, mas devem ser contados. Escrever as listas V, A e B. Escrever
#quantos elementos nulos foram encontrados em V.

def lerlista(lista):
    for i in range(5):
        num = int(input('Digite um numero: ')) #Lista de 5 elementos
        lista.append(num)
    return lista

def separar(lista):
    listaA = []
    listaB = []
    soma = 0
    for i in range(len(lista)):
        if lista[i] > 0:
            listaA.append(lista[i])
        elif lista[i] < 0:
            listaB.append(lista[i])
        else:
            soma = soma + 1
    return listaA, listaB, soma

lista = []
lista = lerlista(lista)
listaA, listaB, soma = separar(lista)

print('Lista completa = ' , lista)
print('Lista A = ', listaA)
print('Lista B = ', listaB)
print('Total de zeros na lista = ', soma)