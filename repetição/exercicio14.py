''''
Crie um programa que solicite ao usuário 10 valores, apresente o maior valor lido e a
posição (1o, 2o, 3o, etc.) em que o mesmo foi informado.
'''

#Pedindo ao usuário o primeiro número
primeiro_valor = float(input('Digite um numero: '))
maior_valor = primeiro_valor
posicao = 1 #Declarando a posição 1, caso o maior número seja o primeiro digitado

#Estrutura de repetição
for i in range(2,11,1):
    num = float(input('Digite um numero: '))
    if num > maior_valor:
        posicao = i
        maior_valor = num

#Exibindo resultados
print('Posicao:', posicao)
print('Maior valor: ', maior_valor)
