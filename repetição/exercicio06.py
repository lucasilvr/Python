#Construa um programa que leia vários números e informe quantos números entre 100
#e 200 foram digitados. Quando o valor 0 (zero) for lido, o programa deverá cessar sua
#execução.

contador = 0

num = 1
while num != 0:
    if num >= 100 and num <=200:
        contador = contador + 1
    num = float(input('Digite um numero: '))

print('Foram digitados', contador, 'numeros que estão entre 100 e 200')

