import math
num = int(input('digite um numero: '))
if num > 0:
    raiz = math.sqrt(num)
    print('raiz quadrada de', num, 'é', raiz)
elif num < 0:
    quadrado = num ** 2
    print('o',num,'ao quadrado é:',quadrado)
else:
    print('numero igual a 0')

