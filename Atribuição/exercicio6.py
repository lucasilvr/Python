# Faça um programa que receba o salário-base de um funcionário, calcule e
# mostre o salário a receber, sabendo-se que esse funcionário tem gratificação
# de 5% sobre o salário-base e paga imposto de 7% sobre o salário-base.

#Solicitando ao usuário as informações
salario_base = float(input('Digite seu salário base: R$ '))

#Cálculo
gratificacao = salario_base * 0.05
imposto = salario_base * 0.07
salario_final = (salario_base + gratificacao) - imposto

#Exibindo resultados
print('Salário base: R$ %.2f' % salario_base)
print('Gratificação: %.2f' % gratificacao)
print('Imposto: %.2f' % imposto)
print('Salario final: R$ %.2f' % salario_final)
