# Faça um programa que receba o salário de um funcionário e o percentual de aumento, calcule e mostre
# o valor do aumento e o novo salário.

#Solicitando as informações ao usuário
salario = float(input('Digite seu salário: R$ '))
aumento = float(input('Digite o percentual de aumento: '))

#Cálculo
novo_salario = salario + (salario * aumento)

#Exibindo resultados
print('Antigo salário: R$ %.2f,' % salario, 'Novo salário: R$ %.2f' % novo_salario)