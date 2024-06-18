def ler(lista):
    num = int(input('Digite umn numero: 0 para sair: '))
    while num != 0:
        lista.append(num)
        num = int(input('Digite um número: 0 para sair: '))
    return lista

def valorS(lista):  #Lista[5, 6, 7, 8] # 1/5 + 2/6 + 3/7 + 4/8 (excluindo o índice 0) - exemplo
    soma = 0
    for i in range(1, len(lista), 1):
        soma = soma + (i/lista[i])
    return soma

def numeradorInf(lista):
    soma = 0
    for i in range(1, len(lista), 1):
        if i < lista[i]:
            soma = soma + 1
    return soma

lista = []
lista = ler(lista)
valorS = valorS(lista)
numeradorInf = numeradorInf(lista)
print('A lista', lista)
print('Valor de S (Soma dos índice/elemento [excluindo o índice 0]: %.1f ' % valorS)
print('Quantos termos tem o numerador inferior ao denominador: ', numeradorInf)