precoEtiqueta = float(input('informe o preço da etiqueta: '))
codigo = int(input('\n1 - À vista em dinheiro ou cheque, recebe 10% de desconto\n'
                   '2 - À vista no cartão de crédito, recebe 5% de desconto\n'
                   '3- Em duas vezes, preço normal da etiqueta sem juros\n'
                   '4 - Em três vezes, preço normal da etiqueta mais juros de 5%\n\n'
                   'Informe o numero do código que deseja: '))

if codigo == 1:
    desconto = (precoEtiqueta * 0.10)
    valor = precoEtiqueta - desconto
    