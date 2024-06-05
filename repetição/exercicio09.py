'''
Construa um programa que calcule e imprima a média aritmética de vários valores
inteiros positivos, lidos externamente. O final da leitura acontecerá quando for lido um
valor negativo.
'''

valor_1 = int(input('Insira um valor: '))
valor_2 = int(input('Insira um valor: '))

while valor_1 > 0 and valor_2 > 0:
    media = (valor_1 + valor_2)/2
    print(media)
    valor_1 = int(input('Insira um valor: '))
    valor_2 = int(input('Insira um valor: '))

print('Fim do programa pois foi lido um número negativo')