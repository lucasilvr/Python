salario = float(input('digite seu salario: R$ '))

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