'''

A série de Fibonacci é formada pela seguinte seqüência:”1,1,2,3,5,8,113, 21, 34, 55, ...
etc”. Escreva um programa que gere a série de Fibonacci até o vigésimo termo.

A sequência de Fibonacci é uma sequência numérica em que cada número seguinte é a soma dos dois anteriores, iniciando por 0

'''

num = 0

for i in range (1,21,1):
    fibo = num + i
    num = fibo
    print(fibo)

#Não consegui terminar professor, achei dificil
