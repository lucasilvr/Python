# Faça um programa que leia 3 número inteiros diferentes e escreva-os em ordem decrescente

#Solicitando dados ao usuário
num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite um número inteiro: '))
num3 = int(input('Digite um número inteiro: '))

#Verificando a ordem decrescente
if num1 > num2 and num1 > num3 and num2 > num3: #1,2,3
    print(num1, num2, num3)
elif num1 > num2 and num1 > num3 and num3 > num2: #1, 3, 2
    print(num1, num3, num2)
elif num2 > num1 and num2 > num3 and num3 > num1:   #2, 3, 1
    print(num2, num3, num1)
elif num2 > num1 and num2 > num3 and num1 > num3: #2, 1, 3
    print(num2, num1, num3)
elif num3 > num1 and num3 > num2 and num2 > num1: #3, 2, 1
    print(num3, num2, num1)
elif num3 > num1 and num3 > num2 and num1 > num2: #3, 1, 2
    print(num3, num1, num2)
