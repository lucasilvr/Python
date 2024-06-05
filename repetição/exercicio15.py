'''
Dado um país A, com 5 milhões de habitantes e uma taxa de natalidade de 3% ao
ano, e um país B com 7 milhões de habitantes e uma taxa de natalidade de 2% ao
ano, crie um programa que calcule e imprima o tempo necessário para que a
população do país A ultrapasse a população do país B.
'''


A = 5_000_000
B = 7_000_000
tempo = 0

while A <= B:
    A = A + (A * 0.03)
    B = B + (B * 0.02)
    tempo = tempo + 1

print('São necessários', tempo,'anos')