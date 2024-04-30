# Crie um programa que leia um número e imprima a raiz quadrada do número caso ele seja positivo e o
# quadrado do número caso ele seja negativo.
# Obs. Não se esqueça de tratar o caso do número ser igual a zero

#Biblioteca
import math

#Solicitando dado ao usuário
num = int(input('Digite um número: '))

#Condição
if num > 0:
    raiz = math.sqrt(num)
    print('Raiz quadrada de', num, 'é', raiz)
elif num < 0:
    quadrado = num ** 2
    print('O',num,'ao quadrado é:',quadrado)
else:
    print('Número igual a 0')

