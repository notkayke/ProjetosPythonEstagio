import json

# Exemplo de dados de faturamento em JSON
dados = '''
[
    {"dia": 1, "valor": 1000.0},
    {"dia": 2, "valor": 2000.0},
    {"dia": 3, "valor": 0.0},
    {"dia": 4, "valor": 6000.0},
    {"dia": 5, "valor": 5000.0}
]
'''

faturamento = json.loads(dados)

valores = [dia["valor"] for dia in faturamento if dia["valor"] > 0]
menor_valor = min(valores)
maior_valor = max(valores)
media_mensal = sum(valores) / len(valores)
dias_acima_da_media = sum(1 for valor in valores if valor > media_mensal)

print(f"Menor valor de faturamento: R${menor_valor:.2f}")
print(f"Maior valor de faturamento: R${maior_valor:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")
