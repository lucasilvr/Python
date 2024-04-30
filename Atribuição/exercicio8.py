# Faça um programa que receba o ano de nascimento de uma pessoa e o ano
# atual, calcule e mostre:
# − a idade dessa pessoa;
# − quantos anos essa pessoa tem.

#Solicitando dados ao usuário
ano_nascimento = int(input('Digite seu ano de nascimento: '))
ano_atual = int(input('Digite o ano atual: '))

#Cálculo
idade = ano_atual - ano_nascimento

#Exibindo resultados
print('Você tem', idade, 'anos')