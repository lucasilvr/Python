nota1 = float(input('digite sua primeira nota: '))
nota2 = float(input('digite sua segunda nota: '))
media = (nota1 + nota2)/2

if media >= 7.0:
    print('Aprovado com média: %.1f' % media)
elif media < 7.0 and media >= 3.0:
    print('Exame com média: %.1f' % media)
else:
    print('Reprovado com média: %.1f' % media)