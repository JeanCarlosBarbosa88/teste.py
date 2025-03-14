faturamento_estados ={
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "OUTROS": 19849.53
}

# calcular o faturamento
total_faturamento = sum(faturamento_estados.values())

# calcular dos porcentagem
percentuais = {estado: (faturamento / total_faturamento) * 100 for estado, faturamento in faturamento_estados.items()}

#exibindo resultados
for estado, percetual in percentuais.items():
    print(f"{estado}: {percetual:.2f}%")
