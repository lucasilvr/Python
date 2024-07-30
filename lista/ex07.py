#Faça um programa em Python para ler, por meio de uma função, uma lista V
#de elementos inteiros, que representa um vetor e gere um novo vetor que
#represente a multiplicação por um escalar (um número). Imprima os vetores
#e o valor escalar.

def ler(vetor):
    num = input('Digite um numero [aperte o enter vazio para sair]: ')
    while True:
        if num == '':
            break
        else:
            vetor.append(num)
            num = input('Digite um numero [aperte o enter vazio para sair]: ')
    return vetor

def multEscalar(vetor, vetor_escalar, num):
    for i in range(len(vetor)):
        aux = vetor[i]
        aux2 = int(aux) #Transformando a variável aux em um número inteiro, pois a variável estava sendo tratado como String
        aux = aux2 * num
        vetor_escalar.append(aux)
    return vetor_escalar

vetor = []
vetor = ler(vetor)

num = int(input('Informe o número escalar: '))

vetor_escalar = []
vetor_escalar = multEscalar(vetor, vetor_escalar, num)

print('\nVetor = ', vetor)
print('Vetor após a multiplicação escalar = ', vetor_escalar)
print('Valor escalar = ', num)



