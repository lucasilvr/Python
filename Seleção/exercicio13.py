'''
Tendo como dados de entrada a altura (h) e o sexo de uma pessoa, construa um programa que calcule e imprima
seu peso ideal, utilizando as seguintes fórmulas:
para homens: (72.7*h) – 58;
para mulheres: (62.1*h) – 44.7.
'''

#Pedindo dados ao usuário
altura = float(input('Digite sua altura: '))
sexo = str(input('Digite sua sexualidade, homem ou mulher: '))

#Verificando o sexo para realizar o cálculo
if sexo == 'homem':
    peso = (72.7 * altura) - 58
    print('Peso ideal:', peso)
elif sexo == 'mulher':
    peso = (62.1 * altura) - 44.7
    print('Peso ideal: ', peso)
else:
    print('Erro de digitação')
