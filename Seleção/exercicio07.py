# Crie um programa que leia 2 notas de um aluno e calcule a média. Se a média do aluno for maior que 7.0,
# escreva 'Aprovado'; se for menor que 7.0 mas maior que 3.0, escreva 'Exame'; se for menor que 3.0, escreva
# 'Reprovado'. Além da mensagem, informe também qual foi a média do aluno.

#Solicitando os dados ao usuário
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2)/2

#Condição
if media >= 7.0:
    print('Aprovado com média: %.1f' % media)
elif media < 7.0 and media >= 3.0:
    print('Exame com média: %.1f' % media)
else:
    print('Reprovado com média: %.1f' % media)