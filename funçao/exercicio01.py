'''
Rescreva o programa abaixo que exclui o primeiro elemento da lista com
valor especificado, mas utilizando uma função.
lista = [1, 4, 5, 6, 4, 7]
valor = 4
removeu = False
temp = []
for i in range(len(lista)):
    if lista[i] != valor or removeu:
        temp.append(lista[i])
    else:
        removeu = True
lista = temp
print(lista)
'''

#Função para remover elemento
def removerElemento(lista):
    valor = 4
    removeu = False
    temp = []
    for i in range(len(lista)):
        if lista[i] != valor or removeu: #Removeu usado para garantir que apenas o primeiro 4 seja removido
            temp.append(lista[i])
        else:
            removeu = True #Transformou o removeu em True
    return temp

#Programa Principal
lista = [1, 4, 5, 6, 4, 7]
lista = removerElemento(lista)
print(lista)