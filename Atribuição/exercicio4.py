# Faça um programa que leia o salário de um funcionário, calcule e mostre seu novo salário, sabendo-se que
# o funcionário recebeu um aumento de 25%.

#Solicitando ao usuário o salário
salario = float(input('Digite seu salário: R$ '))

#Cálculo
aumento = salario + (salario * 0.25)

#Exibindo resultados
print('Antigo salário: R$ %.2f,' % salario, 'Novo salario: R$ %.2f' % aumento)