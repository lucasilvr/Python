'''
Construa um programa que leia o preço e o código de origem do produto e imprima seu preço e sua
procedência, de acordo com a tabela abaixo. Caso o código não seja nenhum dos especificados, o produto
deve ser encarado como 'importado'. Se o produto for importado, deverá também ser calculado e apresentado
o preço acrescido de 15%, correspondente ao imposto de importação.

Código Procedência
1 Sudeste
2 Sul
3 Centro-Oeste
4 Nordeste
5 Norte
'''

#Solicitando dados ao usuário
produto_preco = float(input('Digite o preço do produto: '))
produto_codigo = int(input('Digite o código do produto: '))

#Verificando qual o código de procedência
if produto_codigo == 1:
    print('\nPreço:', produto_preco)
    print('Procedência sudeste')
elif produto_codigo == 2:
    print('\nPreço:', produto_preco)
    print('Procedência sul')
elif produto_codigo == 3:
    print('\nPreço:', produto_preco)
    print('Procedência centro-oeste')
elif produto_codigo == 4:
    print('\nPreço:', produto_preco)
    print('Procedência nordeste')
elif produto_codigo == 5:
    print('\nPreço:', produto_preco)
    print('Procedência norte')
else:
    imposto = produto_preco * 0.15
    produto_preco = produto_preco + imposto
    print('\nPreço com imposto de importação:', produto_preco)
    print('Produto importado')