def analise_vendas(vendas):
    # Calcule o total de vendas
    total_vendas = sum(vendas)
    # Calcule a média mensal de vendas
    media_vendas = total_vendas / len(vendas)
    
    return f"{total_vendas}, {media_vendas:.2f}"

def obter_entrada_vendas():
    # Solicita a entrada do usuário em uma única linha
    entrada = input("")
    # Converte a entrada em uma lista de inteiros
    vendas = list(map(int, entrada.split(',')))
    
    return vendas

# Obtém as vendas do usuário
vendas = obter_entrada_vendas()
# Imprime a análise de vendas
print(analise_vendas(vendas))
