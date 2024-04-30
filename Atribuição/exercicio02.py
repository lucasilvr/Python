# Faça um programa que leia 3 notas, calcule e mostre a média aritmética entre elas.

#Solicitando ao usuário as notas
nota1 = float(input('nota 1: '))
nota2 = float(input('nota 2: '))
nota3 = float(input('nota 3: '))

#Cálculo
total = (nota1 + nota2 + nota3)/3

#Exibindo resultados
print('%.2f'% total)
