# Faça um programa que receba o ano de nascimento de uma pessoa e o ano
# atual, calcule e mostre:
# − a idade dessa pessoa;
# − quantos anos essa pessoa tem.

ano_nascimento = int(input('digite seu ano de nascimento: '))
ano_atual = int(input('digite o ano atual: '))

idade = ano_atual - ano_nascimento
print('você tem', idade, 'anos')