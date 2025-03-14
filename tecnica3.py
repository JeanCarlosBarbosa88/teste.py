import json

# carregar o arquivo
with open('faturamento.json', 'r') as arquivo:
    dados = json.load(arquivo)
    faturamento = dados["faturamento"]
    custo = dados["custo"]
    
# remoção dias sem faturamento
faturamento_validos = [valor for valor in faturamento if valor != 0]

# calcular o faturamento
menor_faturamento = min(faturamento_validos)
maior_faturamento = max(faturamento_validos)
total_faturamento = sum(faturamento_validos)
media_faturamento = total_faturamento / len(faturamento_validos)

# dias com faturamento acima da média
dias_acima_media = [dia for dia in faturamento if dia > media_faturamento]

# exibir os resultados
print(f"O menor faturamento foi de R${menor_faturamento}")
print(f"O maior faturamento foi de R${maior_faturamento}")
print(f"O total faturamento foi de R${total_faturamento}")
print(f"A média faturamento foi de R${media_faturamento}")
print(f"Os dias com faturamento acima da média são: {dias_acima_media}")