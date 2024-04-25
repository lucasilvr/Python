num1 = float(input('digite o primeiro numero: '))
num2 = float(input('digite o segundo numero: '))
num3 = float(input('digite o terceiro numero: '))

if num1 > num2 and num1 > num3:
    print(f'o maior numero é {num1}')
elif num2 > num1 and num2 > num3:
    print(f'o maior numero é {num2}')
else:
    print(f'o maior numero é {num3}')