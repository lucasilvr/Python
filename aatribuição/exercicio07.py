# Faça um programa que calcule e mostre a área de um círculo.

#Biblioteca
import math

#Cálculo
raio = int(input('Digite o raio do círculo: '))
area = math.pi * raio ** 2
print('A área do círculo é: %.1f' % area)