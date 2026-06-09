import json
from datetime import datetime
from relatorios import atualizar_historico

def registrar_venda(filme_id, quantidade):
    with open("filmes.json", "r", encoding='utf-8') as arquivo:
        filmes = json.load(arquivo)
        
    filme_encontrado = None
    
    for filme in filmes:
        if filme['id'] == filme_id:
            filme_encontrado = filme
            break
        
    if not filme_encontrado:
        print(f"Filme não encontrado")
        return
        
    if filme_encontrado['estoque'] < quantidade:
        print(f"Esquece, estoque insuficiente. Disponível atualmente: {filme_encontrado['estoque']}")
        return
    
    filme_encontrado['estoque'] -= quantidade
    
    with open("filmes.json", "w", encoding='utf-8') as arquivo:
        json.dump(filmes, arquivo, indent=2)
    
    preco = filme_encontrado['preco_promocional'] if filme_encontrado["preco_promocional"] is not None else filme_encontrado["preco"]
    
    with open("vendas.json", "r", encoding='utf-8') as arquivo:
        vendas = json.load(arquivo)
        
    novo_id = vendas[-1]['id'] + 1 if vendas else 1
    
    nova_venda = {
        "id": novo_id,
        "filme_id": filme_id,
        "titulo": filme_encontrado["titulo"],
        "quantidade": quantidade,
        "preco_unitario": preco,
        "total": round(preco * quantidade, 2),
        "data_hora": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }
    
    vendas.append(nova_venda)
    
    with open("vendas.json", "w", encoding='utf-8') as arquivo:
        json.dump(vendas, arquivo, indent=2)
        
    print(f"Venda registrada! {quantidade}x {filme_encontrado['titulo']} | Total: R$ {nova_venda['total']:.2f}")

    atualizar_historico(filme_encontrado['titulo'], quantidade)
