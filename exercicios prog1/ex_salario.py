'''
2) Dado o nome e o salário bruto de um funcionário, imprimir: o nome, o salário
bruto, a margem de desconto, o valor do desconto e o salário líquido do
funcionário. O desconto será obtido: se o salário bruto for menor ou igual a
R$1000,00 a margem de desconto será de 10%, caso contrário a margem de
desconto será de 15%.
'''

nome_funcionario = str(input('Informe seu nome: '))
salario_bruto = float(input(('Informe seu salário bruto: R$ ')))

if salario_bruto <= 1000:
    desconto = salario_bruto * 0.10
    salario_liquido = salario_bruto - desconto
    margem = '10%'
else:
    desconto = salario_bruto * 0.15
    salario_liquido = salario_bruto - desconto
    margem = '15%'

print('\nNome do funcionário:', nome_funcionario)
print('Salário bruto: R$', salario_bruto)
print('Margem do desconto: ', margem)
print('Valor do desconto: ', desconto)
print('Salário líquido: ', salario_liquido)
