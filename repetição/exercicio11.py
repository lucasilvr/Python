'''
Crie um programa que receba o valor e o código de várias mercadorias vendidas em
um determinado dia. Os códigos obedecem à lista a seguir:
'L': limpeza 'A': alimentação 'H': higiene

Calcule e imprima o total vendido naquele dia para cada um dos códigos e o total
vendido para todos os códigos juntos. Para encerrar a entrada de dados, digite o valor
da mercadoria 0 (zero).
'''

#Declaração de algumas variáveis
valor_l = 0
valor_a = 0
valor_h = 0
valor_total = 0
valor = 1

#Estrutura de repetição
while valor != 0:
    #Solicitando dados ao usuário
    valor = float(input('Digite o valor da mercadoria: '))
    codigo = str(input('\nL - para limpeza\nA - para alimentação\nH - para higiene\nDigite: '))
    #Condição
    if codigo == 'L':
        valor_l = valor_l + valor
        valor_total = valor_total + valor

    elif codigo == 'A':
        valor_a = valor_a + valor
        valor_total = valor_total + valor

    elif codigo == 'H':
        valor_h = valor_h + valor
        valor_total = valor_total + valor
    else:
        print('Código Inválido')

#Exibindo os resultados
print('\nTotal vendido em Limpeza: R$', valor_l)
print('Total vendido em Alimentação: R$', valor_a)
print('Total vendido em Higiene: R$', valor_h)
print('Valor total', valor_total)


#A estrutura do while pode também ser assim
'''
  while True:
  valor = float(input('Digite o valor da mercadoria: '))
  if valor == 0:
      break
  codigo = str(input('\nL - para limpeza\nA - para alimentação\nH - para higiene\nDigite: '))
'''