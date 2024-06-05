'''

Construa um programa que funcione através do seguinte menu (o programa deve
apresentar o menu ao usuário e, dependendo da opção escolhida, realizar a operação
correspondente):
MAQUINA ESPERTA
1 – Soma vários números
2 – Multiplica vários números
3 – Sai do programa
DIGITE A OPÇÃO:

Para terminar as repetições nas opções 1 e 2, use um número pequeno, como -0,0001

'''

maquina_esperta = 0

while maquina_esperta != 3:
    maquina_esperta = int(input('MAQUINA ESPERTA\n1 - Soma vários números\n2 - Multiplica varios numeros\n3 - Sai do programa\nDigite: '))

    if maquina_esperta == 1:
        soma = 0
        num = 0
        num = float(input('Digite um numero: '))
        while num != -0.0001:
            soma = soma + num
            print('Total:', soma)
            num = float(input('Digite um numero: '))

    if maquina_esperta == 2:
        soma = 1
        num = 0
        num = float(input('Digite um numero: '))
        while num != -0.0001:
            soma = soma * num
            print('Total:', soma)
            num = float(input('Digite um número: ' ))

    if maquina_esperta == 3:
        print("Saiu do programa")