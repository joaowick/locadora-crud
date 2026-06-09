import os
import json

def iniciar_arquivos():
    if not os.path.exists("filmes.json"):
        with open("filmes.json", "w", encoding='utf-8') as arquivo:
            json.dump([], arquivo)
        print("Arquivo filmes.json criado automaticamente.")
    else:
        print("Arquivo filmes.json já existente.")
        
    if not os.path.exists("vendas.json"):
        with open("vendas.json", "w", encoding='utf-8') as arquivo:
            json.dump([], arquivo)
        print("Arquivo vendas.json criado automaticamente.")
    else:
        print("Arquivo vendas.json já existente.")
        
def listar_filmes():
    with open("filmes.json", "r", encoding='utf-8') as arquivo:
        filmes = json.load(arquivo)
        
    if not filmes:
        print("Nenhum filme cadastrado.")
        return
    
    for filme in filmes:
        preco = f"R$ {filme['preco_promocional']:.2f} (PROMOÇÃO)" if filme['preco_promocional'] is not None else f"R$ {filme['preco']:.2f}"
        print(f"ID: {filme['id']} | {filme['titulo']} | {filme['diretor']} | {filme['ano']} | {filme['genero']} | {preco} | Estoque: {filme['estoque']}")

def cadastrar_filme(titulo, diretor, ano, genero, preco, estoque):
    with open("filmes.json", "r", encoding='utf-8') as arquivo:
        filmes = json.load(arquivo)
        
    if filmes:
        novo_id = filmes[-1]["id"] + 1
    else:
        novo_id = 1
        
    novo_filme = {
        "id": novo_id,
        "titulo": titulo,
        "diretor": diretor,
        "ano": ano,
        "genero": genero,
        "preco": preco,
        "estoque": estoque,
        "preco_promocional": None
    }
    
    filmes.append(novo_filme)
    
    with open("filmes.json", "w", encoding='utf-8') as arquivo:
        json.dump(filmes, arquivo, indent=2)
    
    print(f"Filme '{titulo}' cadastrado com sucesso!")

def pesquisar_filme(categoria, valor):
    with open("filmes.json", "r", encoding='utf-8') as arquivo:
        filmes = json.load(arquivo)
    
    encontrado = []
    
    for filme in filmes:
        if categoria == "titulo" and valor.lower() in filme["titulo"].lower():
            encontrado.append(filme)
        if categoria == "diretor" and valor.lower() in filme["diretor"].lower():
            encontrado.append(filme)
        if categoria == "ano" and str(valor) == str(filme["ano"]):
            encontrado.append(filme)
            
    if encontrado:
        for filme in encontrado:
            print(f"ID: {filme['id']} | {filme['titulo']} | {filme['diretor']} | {filme['ano']} | {filme['genero']} | {filme['preco']:.2f} | Estoque: {filme['estoque']}")
    else:
        print(f"'{valor}' não encontrado.")
        
def alterar_preco(id, novo_preco):
    with open("filmes.json", "r", encoding='utf-8') as arquivo:
        filmes = json.load(arquivo)
        
    encontrado = False
    
    for filme in filmes:
        if filme['id'] == id:
            filme['preco'] = novo_preco
            encontrado = True
            break
    
    if not encontrado:
        print(f"ID {id} não encontrado.")
        return
    
    with open("filmes.json", "w", encoding='utf-8') as arquivo:
        json.dump(filmes, arquivo, indent=2)
        
    print(f"Preço atualizado com sucesso!")

def adicionar_estoque(id, quantidade):
    with open("filmes.json", "r", encoding='utf-8') as arquivo:
        filmes = json.load(arquivo)
        
    encontrado = False
    
    for filme in filmes:
        if filme['id'] == id:
            filme['estoque'] += quantidade
            encontrado = True
            break
    
    if not encontrado:
        print(f"ID {id} não encontrado.")
        return
    
    with open("filmes.json", "w", encoding='utf-8') as arquivo:
        json.dump(filmes, arquivo, indent=2)
        
    print(f"Estoque do filme {filme['titulo']} atualizado com sucesso.")
    
def promocao_filme(id, desconto):
    with open("filmes.json", "r", encoding='utf-8') as arquivo:
        filmes = json.load(arquivo)
        
    encontrado = False
    
    for filme in filmes:
        if filme['id'] == id:
            filme['preco_promocional'] = round(filme['preco'] - (filme['preco'] * desconto / 100), 2)
            encontrado = True
            break
        
    if not encontrado:
        print(f"ID {id} não encontrado.")
        return
    
    with open("filmes.json", "w", encoding='utf-8') as arquivo:
        json.dump(filmes, arquivo, indent=2)
        
    print(f"Promoção aplicada com sucesso!")

def promocao_todos(desconto):
    with open("filmes.json", "r", encoding='utf-8') as arquivo:
        filmes = json.load(arquivo)
        
    for filme in filmes:
        filme['preco_promocional'] = round(filme['preco'] - (filme['preco'] * desconto / 100), 2)
        
    with open("filmes.json", "w", encoding='utf-8') as arquivo:
        json.dump(filmes, arquivo, indent=2)
        
    print(f"Promoção aplicada em todos os filmes com sucesso!")

def cancelar_promo_filme(id):
    with open("filmes.json", "r", encoding='utf-8') as arquivo:
        filmes = json.load(arquivo)
    
    encontrado = False
    
    for filme in filmes:
        if filme['id'] == id:
            filme['preco_promocional'] = None
            encontrado = True
            break
        
    if not encontrado:
        print(f"ID {id} não encontrado.")
        return
    
    with open("filmes.json", "w", encoding='utf-8') as arquivo:
        json.dump(filmes, arquivo, indent=2)
        
    print(f"Promo de filme {filme['titulo']} é cancelado")

def cancelar_promo_todos():
    with open("filmes.json", "r", encoding='utf-8') as arquivo:
        filmes = json.load(arquivo)
        
    for filme in filmes:
        filme['preco_promocional'] = None
        
    with open("filmes.json", "w", encoding='utf-8') as arquivo:
        json.dump(filmes, arquivo, indent=2)
        
    print(f"As promoções de todos os filmes são cancelados")

def deletar_filme(id):
    with open("filmes.json", "r", encoding='utf-8') as arquivo:
        filmes = json.load(arquivo)
        
    encontrado = False
    
    nova_lista = []
    
    for filme in filmes:
        if filme['id'] == id:
            titulo_deletado = filme['titulo']
            encontrado = True
        else:
            nova_lista.append(filme)
            
    if not encontrado:
        print(f"ID {id} não encontrado.")
        return        
            
    filmes = nova_lista
    
    with open("filmes.json", "w", encoding='utf-8') as arquivo:
        json.dump(filmes, arquivo, indent=2)
        
    print(f"Filme '{titulo_deletado}' deletado com sucesso!")

def buscar_filme_por_id(id):
    with open("filmes.json", 'r', encoding='utf-8') as arquivo:
        filmes = json.load(arquivo)

    for filme in filmes:
        if filme['id'] == id:
            return filme
    
    return None