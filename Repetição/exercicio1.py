#Crie um programa que leia 20 valores e escreva o seu somatório.

#Inicializa a variável soma
soma = 0

#Solicita ao usuário que insira os valores
for i in range(1,21,1):
    valor = float(input('Digite um valor: '))
    soma = soma + valor

#Exibe o resultado
print('Soma = ', soma)
