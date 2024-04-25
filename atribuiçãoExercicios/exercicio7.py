# Faça um programa que calcule e mostre a área de um círculo.

import math

raio = int(input('digite o raio do círculo: '))
area = math.pi * raio ** 2
print('a area do círculo é: %.1f' % area)