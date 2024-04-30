#Crie um programa que leia 6 números inteiros positivos e escreva o maior deles.

#Inicializa a variável
numero_maior = 0

#Solicita ao usuário que insira os valores inteiros positivos
for i in range(1,7):
    numero = int(input('Digite um numero inteiro positivo: '))
    if numero > numero_maior:
        numero_maior = numero
    elif numero == 0 or numero < 0: #Programação defensiva
        print('Digitou um número 0 ou negativo')
        break

#Exibe o resultado
if numero > 0:
    print('Número maior:', numero_maior)


