# População inicial e taxas de crescimento
populacao_A = 5_000_000  # 5 milhões de habitantes
taxa_natalidade_A = 0.03  # 3% ao ano

populacao_B = 7_000_000  # 7 milhões de habitantes
taxa_natalidade_B = 0.02  # 2% ao ano

# Contador de anos
anos = 0

# Loop até a população do país A ultrapassar a do país B
while populacao_A <= populacao_B:
    # Atualiza as populações para o próximo ano
    populacao_A += populacao_A * taxa_natalidade_A
    populacao_B += populacao_B * taxa_natalidade_B
    # Incrementa o contador de anos
    anos += 1

# Imprime o número de anos necessários
print(f"A população do país A ultrapassará a população do país B em {anos} anos.")
