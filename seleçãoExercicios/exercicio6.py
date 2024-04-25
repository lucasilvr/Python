idade = int(input('digite sua idade: '))
if idade >= 18 and idade < 65:
    print('\nvocê é maior de idade')
elif idade < 18:
    print('\nvocê é menor de idade')
else:
    print('\nvocê tem mais de 65 anos')