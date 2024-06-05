#Crie um programa que leia um número inteiro positivo e encontre o fatorial deste número.

#Inicializa a variável
fatorial = 1

#Solicita ao usuário o número fatorial
numero = int(input('Digite um número inteiro positivo: '))
if numero > 0:
    for i in range(1, numero + 1): #Começa em 1 e termina com o número + 1 pois inclui o próprio número (se começasse com 0 ia dar problema)
        fatorial = fatorial * i

# Programação defensiva
elif numero < 0:
    print('Você digitou um número negativo')
elif numero == 0:
    print('Você digitou zero')

#Exibe os resultados
if numero > 0:
    print(f'Fatorial de {numero} é: {fatorial}')