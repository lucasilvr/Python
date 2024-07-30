#Faça um programa em Python para ler, por meio de uma função, uma lista V
#de elementos inteiros e utilizando outra função, verificar se a soma dos
#elementos pares da lista V é igual a soma dos elementos ímpares da lista V,
#a função deve retornar um valor booleano. Imprimindo mensagens
#adequadas.

def lerLista(lista):
    num = int(input('Digite um numero: 0 para sair: '))
    while num != 0:
        lista.append(num)
        num = int(input('Digite um número: 0 para sair: '))
    return lista

def somaPar(lista):
    par = 0
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            par = par + lista[i]
    return par
def somaImpar(lista):
    impar = 0
    for i in range(len(lista)):
        if lista[i] % 2 != 0:
            impar = impar + lista[i]
    return impar

def somaElementos(par, impar):
    if par == impar:
        return True
    else:
        return False

lista = []
lista = lerLista(lista)

par = somaPar(lista)
impar = somaImpar(lista)

soma = somaElementos(par, impar)

if soma == True:
    print('A soma dos elementos pares da lista é IGUAL a soma dos elementos ímpares')
else:
    print('A soma dos elementos pares da lista é DIFERENTE a soma dos elementos ímpares')










