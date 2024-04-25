# Faça um programa que leia o salário de um funcionário, calcule e mostre seu novo salário, sabendo-se que
# o funcionário recebeu um aumento de 25%.

salario = float(input('digite seu salário: R$ '))
aumento = salario + (salario * 0.25)
print('antigo salário: R$ %.2f,' % salario, 'novo salario: R$ %.2f' % aumento)