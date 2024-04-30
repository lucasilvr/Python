'''Faça um programa que leia o salário de uma pessoa e imprima o desconto do INSS segundo a tabela a seguir:
menor ou igual a R$ 600,00 isento
maior que R$ 600,00 e menor ou igual a R$ 1200,00 20%
maior que R$ 1200,00 e menor ou igual a R$ 2000,00 25%
maior que R$ 2000,00 30%
'''

#Solicitando o valor do salário
salario = float(input('digite seu salario: R$ '))

#Verificando qual será o desconto
if salario <= 600:
    print('isento')
elif salario > 600 and salario <= 1200:
    desconto = salario * 0.20
    salario_novo = salario - desconto
    print(f'R$ {salario} com desconto de R$ {desconto} fica R$ {salario_novo}')
elif salario > 1200 and salario <= 2000:
    desconto = salario * 0.25
    salario_novo = salario - desconto
    print(f'R$ {salario} com desconto de R$ {desconto} fica R$ {salario_novo}')
else:
    desconto = salario * 0.30
    salario_novo = salario - desconto
    print(f'R$ {salario} com desconto de R$ {desconto} fica R$ {salario_novo}')