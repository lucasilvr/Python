'''
Faça um programa que leia 3 números e verifique se eles podem ou não ser lados de um triângulo. Se podem,
escreva se o triângulo formado é 'equilátero', 'isósceles' ou 'escaleno'. Caso contrário, informe que os números
não compõem um triângulo.
'''

#Pedindo dados para o usuário
num1 = float(input('Digite um número: '))
num2 = float(input('Digite um número: '))
num3 = float(input('Digite um número: '))

#Verificando se é um triângulo e seu tipo
if num1 + num2 > num3 and num2 + num3 > num1 and num3 + num1 > num2:
    if num1 == num2 == num3:
        print('Triângulo Equilátero')
    elif num1 == num2 or num2 == num3 or num3 == num1:
        print('Triângulo Isósceles')
    else:
        print('Triângulo Escaleno')
else:
    print('Os números não formam um triângulo')
