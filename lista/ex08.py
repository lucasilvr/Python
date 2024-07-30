#Faça um programa em Python para ler, por meio de uma função, as duas
#listas U e Y de elementos inteiros, que representam vetores e gere um novo
#vetor que represente a soma de U e Y. Imprima os três vetores.

def ler(vetor):
    num = input('Digite um numero [aperte o enter vazio para sair]: ')
    while True:
        if num == '':
            break
        else:
            vetor.append(num)
            num = input('Digite um numero [aperte o enter vazio para sair]: ')
    return vetor

def vetorMaior(vetor):
    soma = 0
    for i in range(len(vetor)):
        soma = soma + 1
    return soma

def somaVetor(listaU, listaY, novo_vetor, maior):
    for i in range(maior):
        aux = int(listaU[i])
        aux2 = int(listaY[i])
        aux3 = aux + aux2
        novo_vetor.append(aux3)
    return novo_vetor

listaU = []
listaU = ler(listaU)
somaU = vetorMaior(listaU)

listaY = []
listaY = ler(listaY)
somaY = vetorMaior(listaY)

if somaU > somaY:
    maior = somaU
else:
    maior = somaY

novo_vetor = []
novo_vetor = somaVetor(listaU, listaY, novo_vetor, maior)
print(novo_vetor)



