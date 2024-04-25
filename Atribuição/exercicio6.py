# Faça um programa que receba o salário-base de um funcionário, calcule e
# mostre o salário a receber, sabendo-se que esse funcionário tem gratificação
# de 5% sobre o salário-base e paga imposto de 7% sobre o salário-base.

salario_base = float(input('digite seu salario base: R$ '))
gratificacao = salario_base * 0.05
imposto = salario_base * 0.07

salario_final = (salario_base + gratificacao) - imposto
print('salario base: R$ %.2f' % salario_base)
print('gratificação: %.2f' % gratificacao)
print('imposto: %.2f' % imposto)
print('salario final: R$ %.2f' % salario_final)
