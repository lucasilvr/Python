#Escreva um programa que leia um conjunto de 20 números e mostre qual foi o maior e menor valor fornecido.

#Pede o primeiro número ao usuário
primeiro_numero = float(input('Digite um número: '))

#Inicializa as variáveis
maior_numero = primeiro_numero
menor_numero = primeiro_numero

#Solicita ao usuário que insira os números
for i in range(2,21):
    numero = float(input('Digite um número: '))
    if numero > maior_numero:
        maior_numero = numero
    elif numero < menor_numero:
        menor_numero = numero

#Exibi os resultados
print('Maior número =', maior_numero)
print('Menor número =', menor_numero)