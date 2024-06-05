#Construa um programa que permaneça lendo números inteiros enquanto forem positivos
# e que, ao final do programa, informe quantos números foram lidos.

i = 1
contador = 0

while i >= 1:
    num = int(input('Insira um numero inteiro positivo: '))
    i = num
    contador = contador + 1

contador = contador - 1
print('Foram lidos', contador, 'numeros inteiros positivos')

