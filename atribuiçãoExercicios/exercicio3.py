# Faça um programa que leia 3 notas e seus respectivos pesos, calcule e mostre a média ponderada das notas.

nota1 = float(input('digite a nota 1: '))
peso1 = int(input('peso da nota 1: '))

nota2 = float(input('digite a nota 2: '))
peso2 = int(input('peso da nota 2: '))

nota3 = float(input('digite a nota 3: '))
peso3 = int(input('peso da nota 3: '))

pesos = peso1 + peso2 + peso3
calculo = (nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)
media = calculo/pesos
print('a média ponderada das notas é: %.2f' % media)