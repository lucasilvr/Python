#Faça um programa em Python para ler, por meio de uma função, uma lista A
#de elementos inteiros, escreva uma função que gere (crie uma nova) uma
#lista B cujos componentes são os fatoriais dos respectivos componentes de
#A. Imprima as listas A e B.

def lerlista(lista):
    num = int(input('Digite umn numero: 0 para sair: '))
    while num != 0:
        lista.append(num)
        num = int(input('Digite um número: 0 para sair: '))
    return lista

def fatorial(listaA):
    lista = []
    for elemento in range(len(listaA)):
        n = listaA[elemento]
        fat = 1 #Porque se o usuário digitar 0, o fatorial é 1
        i = 2
        while i <= n:
            fat = fat * i
            i = i + 1
        lista.append(fat)
    return lista

print('Lista A')
listaA = []
listaA = lerlista(listaA)

listaB = []
listaB = fatorial(listaA)

print('\nLista A: ', listaA)
print('Lista B: fatoriais dos elementos da lista A: ', listaB)
