'''
Faça um programa que leia um número qualquer. Caso o número seja par menor que 10, escreva ‘Número
parm enor que Dez’, caso o número digitado seja ímpar menor que 10 escreva ‘Número Ímpar menor que Dez’,
caso contrário Escreva ‘Número fora do Intervalo’
'''

#Solicitando dado ao usuário
numero = int(input('Digite um número: '))

#Condição
if numero < 10 and numero % 2 == 0:
    print('Número par menor que 10')
elif numero <10 and numero % 2 != 0:
    print('Número impar menor que 10')
else:
    print('Fora do intervalo')