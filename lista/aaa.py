def ler(vetor):
    entrada = int(input('Digite um numero: '))
    continuar = input('Continuar? [Digite S ou N]: ')
    repetir = True
    while repetir:
        if continuar == "N":
            repetir = False
        elif continuar != 'S' and continuar != 's':
            print('Opção inválida')
            continuar = input('Continuar? [Digite S ou N]: ')
        else:
            vetor.append(entrada)
            entrada = int(input('Digite um numero: '))
            continuar = input('Continuar? [Digite S ou N]: ')
    return vetor

vetor = []
vetor = ler(vetor)
print("Vetor:", vetor)
