# Faça um programa que leia um número e informe se ele é divisível por 3 e por 7

#Solicitando dado ao usuário
numero = int(input('Informe um número: '))

#Condição
if numero % 3 == 0 and numero % 7 == 0:
    print('Divisível por 3 e por 7')
else:
    print('Não é divisível por 3 e por 7')