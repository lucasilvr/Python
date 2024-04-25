numero = int(input('digite um numero: '))
if numero < 10 and numero % 2 == 0:
    print('numero par menor que 10')
elif numero <10 and numero % 2 != 0:
    print('numero impar menor que 10')
else:
    print('fora do intervalo')