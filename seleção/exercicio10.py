# Faça um programa que leia 3 números e imprima se eles podem ou não ser lados de um triângulo.

#Solicitando os dados ao usuário
a = float(input('digite um numero: '))
b = float(input('digite um numero: '))
c = float(input('digite um numero: '))

# condição de existência do triângulo: a soma de quaisquer dois lados do triângulo deve ser maior do que o terceiro lado
if a + b > c and a + c > b and b + c > a:
    print('podem ser lados de um triângulo')
else:
    print('NÃO podem ser lados de um triângulo')