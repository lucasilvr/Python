produto_preco = float(input('digite o preco do produto: '))
produto_codigo = int(input('digite o codigo do produto: '))

if produto_codigo == 1:
    print('\npreço:', produto_preco)
    print('procedencia sudeste')
elif produto_codigo == 2:
    print('\npreço:', produto_preco)
    print('procedencia sul')
elif produto_codigo == 3:
    print('\npreço:', produto_preco)
    print('procedencia centro-oeste')
elif produto_codigo == 4:
    print('\npreço:', produto_preco)
    print('procedencia nordeste')
elif produto_codigo == 5:
    print('\npreço:', produto_preco)
    print('procedencia norte')
else:
    imposto = produto_preco * 0.15
    produto_preco = produto_preco + imposto
    print('\npreco com imposto de importacao:', produto_preco)
    print('produto importado')