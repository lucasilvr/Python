'''
Chico tem 1,50 metro e cresce 2 centímetros por ano, enquanto Zé tem 1,10 metro e
cresce 3 centímetros por ano. Construa um programa que calcule e imprima quantos
anos serão necessários para que Zé seja maior que Chico.
'''

chico = 1.50
zé = 1.10
anos = 0

while zé <= chico:
    chico = chico + 0.02
    zé = zé + 0.03
    anos = anos + 1

print('Serão necessários', anos, 'anos para zé ser maior que chico')
