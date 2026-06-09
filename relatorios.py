# relatorios.py

import json

def painel_bi():
    with open("filmes.json", 'r', encoding='utf-8') as arquivo:
        filmes = json.load(arquivo)

    with open("vendas.json", "r", encoding='utf-8') as arquivo:
        vendas = json.load(arquivo)

    if not filmes:
        print("Nenhum filme encontrado")
        return
    
    if not vendas:
        print("Nenhuma venda registrada")
        return
    
    # Total de vendas e faturamento
    total_vendas = len(vendas)
    faturamento = sum(v['total'] for v in vendas)

    # Filme mais e menos vendido
    vendas_por_filme = {}
    for venda in vendas:
        titulo = venda['titulo']
        vendas_por_filme[titulo] = vendas_por_filme.get(titulo, 0) + venda['quantidade']

    mais_vendido = max(vendas_por_filme, key=lambda x: vendas_por_filme[x])
    menos_vendido = min(vendas_por_filme, key=lambda x: vendas_por_filme[x])

    # Maior e menor estoque
    maior_estoque = max(filmes, key=lambda x: x['estoque'])
    menor_estoque = min(filmes, key=lambda x: x['estoque'])

    print("\n=== PAINEL DE BUSINESS INTELLIGENCE ===")
    print(f"Total de vendas realizadas : {total_vendas}")
    print(f"Faturamento total          : R$ {faturamento:.2f}")
    print(f"Filme mais vendido         : {mais_vendido} ({vendas_por_filme[mais_vendido]} unidades)")
    print(f"Filme menos vendido        : {menos_vendido} ({vendas_por_filme[menos_vendido]} unidades)")
    print(f"Maior estoque              : {maior_estoque['titulo']} ({maior_estoque['estoque']} unidades)")
    print(f"Menor estoque              : {menor_estoque['titulo']} ({menor_estoque['estoque']} unidades)")

def atualizar_historico(titulo, quantidade):
    with open("historico.json", "r", encoding='utf-8') as arquivo:
        historico = json.load(arquivo)

    encontrado = False

    for item in historico:
        if item['titulo'] == titulo:
            item['total_vendido'] += quantidade
            encontrado = True
            break

    if not encontrado:
        historico.append({
            "titulo": titulo,
            "total_vendido": quantidade
        })

    historico.sort(key=lambda x: x['total_vendido'], reverse=True)

    with open("historico.json", "w", encoding='utf-8') as arquivo:
        json.dump(historico, arquivo, indent=2)

def listar_historico():
    with open("historico.json", "r", encoding='utf-8') as arquivo:
        historico = json.load(arquivo)

    if not historico:
        print("Nenhum histórico registrado.")
        return

    print("\n=== HISTÓRICO DE MAIS VENDIDOS ===")
    for i, item in enumerate(historico, start=1):
        print(f"{i}º | {item['titulo']} | {item['total_vendido']} unidades vendidas")