# Escreva um programa que leia um número e escreva se ele é igual a 5, a 200, a 400, se está no intervalo
# entre 500 e 1000, inclusive, ou se ele está fora dos escopos anteriores.

#Solicitando um número ao usuário
num = float(input('digite um numero: '))

#Verificando a condição
if num == 5:
    print('numero igual a 5')
elif num == 200:
    print('numero igual a 200')
elif num == 400:
    print('numero igual a 400')
elif 500 <= num <= 1000:
    print('numero esta no intervalo entre 500 e 1000')
else:
    print('numero esta fora de todos os escopos')