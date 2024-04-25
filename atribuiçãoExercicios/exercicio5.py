# Faça um programa que receba o salário de um funcionário e o percentual de aumento, calcule e mostre
# o valor do aumento e o novo salário.

salario = float(input('digite seu salario: R$ '))
aumento = float(input('digite o percentual de aumento: '))

novo_salario = salario + (salario * aumento)
print('antigo salário: R$ %.2f,' % salario, 'novo salário: R$ %.2f' % novo_salario)