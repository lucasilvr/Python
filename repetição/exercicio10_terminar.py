'''
Em uma entrevista feita com o público em geral foi perguntada a idade, o sexo ('F' ou
'M') e o estado civil ('S' ou 'C') de cada indivíduo. Faça um programa que leia todos os
dados coletados na entrevista. A leitura deverá terminar quando for informado o valor -
1 para a idade. Ao término da leitura, o programa deverá imprimir o percentual de
pessoas do sexo masculino solteiras, o número de mulheres casadas e a idade do
homem mais jovem que seja casado, considerando o conjunto de entrevistados.
'''


idade = 2
contador_m = 0
contador_f = 0
contador_pessoas = 0

while idade > 1:
    idade = int(input('Digite a sua idade: '))
    if idade == 1:
        print('Percentual de pessoas do sexo masculino solteiras:', porcentagem, '%')
        print('Numero de mulheres casadas:', contador_f)
        print('Idade do homem mais jovem que seja casado:', homem_jovem)
    sexo = str(input('Digite o seu sexo\nF mara Feminino ou M para Masculino: '))
    estado_civil = str(input("Digite o seu estado civil\nS para Solteiro ou C para Casado: "))

    contador_pessoas = contador_pessoas + 1

    if sexo == 'M' and estado_civil == 'S':
        contador_m = contador_m + 1
        porcentagem = (contador_pessoas / contador_m) * 100

    elif sexo == 'F' and estado_civil == 'C':
        contador_f = contador_f + 1

    elif sexo == 'M' and estado_civil == 'C':
        homem_jovem = idade
        if idade < homem_jovem:
            homem_jovem = idade

print('percentual', porcentagem)
print('mulheres casadas', contador_f)
print('homem jovem', homem_jovem)




