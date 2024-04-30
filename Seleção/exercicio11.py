'''
Elabore um programa que leia o preço da etiqueta de um produto e o código da condição de pagamento,
calcule e imprima o valor a ser pago pelo cliente de acordo com a tabela a seguir:

Código Condição de pagamento
1 À vista em dinheiro ou cheque, recebe 10% de desconto
2 À vista no cartão de crédito, recebe 5% de desconto
3 Em duas vezes, preço normal da etiqueta sem juros
4 Em três vezes, preço normal da etiqueta mais juros de 5%
'''

#Solicitando o preço do produto ao usuário
precoEtiqueta = float(input('Informe o preço da etiqueta: '))

#Solicitando o código para condição do pagamento
codigo = int(input('\n1 - À vista em dinheiro ou cheque, recebe 10% de desconto\n'
                   '2 - À vista no cartão de crédito, recebe 5% de desconto\n'
                   '3- Em duas vezes, preço normal da etiqueta sem juros\n'
                   '4 - Em três vezes, preço normal da etiqueta mais juros de 5%\n\n'
                   'Informe o numero do código que deseja: '))

#Código de condição do pagamento
if codigo == 1:
    desconto = (precoEtiqueta * 0.10)
    valor = precoEtiqueta - desconto
    print('Valor a pagar: R$', valor)
elif codigo == 2:
    desconto = (precoEtiqueta * 0.05)
    valor = precoEtiqueta - desconto
    print('Valor a pagar: R$', valor)
elif codigo == 3:
    print('Valor a pagar: R$', precoEtiqueta)
elif codigo == 4:
    juros = (precoEtiqueta * 0.05)
    valor = precoEtiqueta + juros
    print('Valor a pagar: R$', valor)