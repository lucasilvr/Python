#Faça um programa que leia a idade de uma pessoa e escreva se a pessoa é 'maior de idade', 'menor de idade'
# ou 'maior de 65 anos'. Apenas uma mensagem deve ser apresentada.

#Solicitando dados ao usuário
idade = int(input('Digite sua idade: '))

#Verificando a idade
if idade >= 18 and idade < 65:
    print('\nVocê é maior de idade')
elif idade < 18:
    print('\nVocê é menor de idade')
else:
    print('\nVocê tem mais de 65 anos')