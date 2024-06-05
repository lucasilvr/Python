'''
Uma empresa irá dar um aumento de salário aos seus funcionários de acordo com a
categoria de cada empregado. O aumento seguirá as seguintes regras:
Funcionários da categoria A ganharão 10% de aumento sobre o salário atual;
Funcionários da categoria B ganharão 15% de aumento sobre o salário atual;
Funcionários da categoria C ganharão 25% de aumento sobre o salário atual;
Funcionários da categoria D ganharão 35% de aumento sobre o salário atual.

Com base nas regras acima, crie um programa para o cálculo do novo salário dos
funcionários. O programa deve ler o salário atual e a categoria do funcionário e
escrever o seu novo salário. A repetição do programa terminará quando for digitado o
valor 0 (zero) para o salário.
'''

#Pedindo dado ao usuário
salario_atual = float(input('\nDigite o seu salário: '))
categoria = int(input('Digite o número de acordo com a sua categoria:\n1 - A\n2 - B\n3 - C\n4 - D\nCategoria: '))

#Estrutura de repetição
while salario_atual != 0: #Poderia usar o break para cortar direto caso o usuário digite 0
    if categoria == 1:
        aumento = salario_atual * 0.10
        salario_novo = salario_atual + aumento
        print('Seu novo salário:', salario_novo)
        salario_atual = float(input('\nDigite o seu salário: '))
        categoria = int(input('Digite o número de acordo com a sua categoria:\n1 - A\n2 - B\n3 - C\n4 - D\nCategoria: '))

    elif categoria == 2:
        aumento = salario_atual * 0.15
        salario_novo = salario_atual + aumento
        print('Seu novo salário:', salario_novo)
        salario_atual = float(input('\nDigite o seu salário: '))
        categoria = int(input('Digite o número de acordo com a sua categoria:\n1 - A\n2 - B\n3 - C\n4 - D\nCategoria: '))


    elif categoria == 3:
        aumento = salario_atual * 0.25
        salario_novo = salario_atual + aumento
        print('Seu novo salário:', salario_novo)
        salario_atual = float(input('\nDigite o seu salário: '))
        categoria = int(input('Digite o número de acordo com a sua categoria:\n1 - A\n2 - B\n3 - C\n4 - D\nCategoria: '))

    elif categoria == 4:
        aumento = salario_atual * 0.35
        salario_novo = salario_atual + aumento
        print('Seu novo salário:', salario_novo)
        salario_atual = float(input('\nDigite o seu salário: '))
        categoria = int(input('Digite o número de acordo com a sua categoria:\n1 - A\n2 - B\n3 - C\n4 - D\nCategoria: '))

    #Caso o usuário digite nenhuma das opções
    else:
        print('Digitou errado')
        salario_atual = float(input('\nDigite o seu salário: '))
        categoria = int(input('Digite o número de acordo com a sua categoria:\n1 - A\n2 - B\n3 - C\n4 - D\nCategoria: '))