'''
1) Sabe-se que:
1 pé = 12 polegadas
1 jarda 3 pés
1 milha = 1760 jardas
Faça um programa que receba uma medida em pés, faça as conversões e
apresente os resultados em (a) polegadas, (b) jardas e (c) milhas.
'''

#Pedindo ao usuário a medida em pés
pes = float(input('Informe a medida em pés: '))

#Cálculo
polegada = pes * 12
jardas = pes / 3
milha = jardas / 1760

#Exibindo resultados
print('\nA medida em polegadas: %.2f' % polegada)
print('A medida em jardas: %.2f' % jardas)
print('A medida em milhas: %.2f' % milha)




