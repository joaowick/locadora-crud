# Atividade João Torres Moreira - Bootcamp Porto

import os
import json
from datetime import datetime

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
        preco = f"R$ {filme['preco_promocional']:.2f} (PROMOÇÃO)" if filme['preco_promocional'] else f"R$ {filme['preco']:.2f}"
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
        
    print(f"Estoque atualizado com sucesso.")
    
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
    
    preco = filme_encontrado['preco_promocional'] if filme_encontrado["preco_promocional"] else filme_encontrado["preco"]
    
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

def menu():
    while True:
        print("\n=== LOCADORA DE FILMES ===")
        print("1 - Listar filmes")
        print("2 - Cadastrar filmes")
        print("3 - Pesquisar filme")
        print("4 - Alterar preço")
        print("5 - Adicionar estoque")
        print("6 - Registrar venda")
        print("7 - Promoção de um filme")
        print("8 - Promoção em todos os filme")
        print("9  - Cancelar promoção de um filme")
        print("10 - Cancelar promoção em todos os filme")
        print("11 - Deletar de um filme")
        print("12 - Iniciar os arquivos")
        print("0 - Sair")
    
        opcao = int(input("\nEscolha uma opção: "))
    

        # listar_filmes()
        if opcao == 1:
            listar_filmes()
        # cadastrar_filme()
        elif opcao == 2:
            titulo = input("Titulo: ")
            diretor = input("Diretor: ")
            ano = int(input("Ano: "))
            genero = input("Genero: ")
            preco = float(input("Preço: "))
            estoque = int(input("Estoque: "))
            cadastrar_filme(titulo, diretor, ano, genero, preco, estoque)
        # pesquisar_filme()
        elif opcao == 3:
            print("Pesquisar categoria por: 1 - Titulo | 2 - Diretor | 3 - Ano")
            sub = int(input("Escolha a categoria: "))
            if sub == 1:
                pesquisar_filme("titulo", input("Titulo: "))
            elif sub == 2:
                pesquisar_filme("diretor", input("Diretor: "))
            elif sub == 3:
                pesquisar_filme("ano", input("Ano: "))
        # alterar_preco()        
        elif opcao == 4:
            id = int(input("ID do filme: "))
            preco = float(input("Novo preço: R$ "))
            alterar_preco(id, preco)
        # adicionar estoque
        elif opcao == 5:
            id = int(input("ID do filme: "))
            quantidade = int(input("Quantidade: "))
            adicionar_estoque(id, quantidade)
        # registrar_venda
        elif opcao == 6:
            id = int(input("ID do filme: "))
            quantidade = int(input("Quantidade: "))
            registrar_venda(id, quantidade)
        # promocao_filme
        elif opcao == 7:
            id = int(input("ID do filme: "))
            desconto = float(input("Desconto (%): "))
            promocao_filme(id, desconto)
        # promocao_todos
        elif opcao == 8:
            desconto = float(input("Desconto (%): "))
            promocao_todos(desconto)
        elif opcao == 9:
            id = int(input("ID do filme: "))
            cancelar_promo_filme(id)
        elif opcao == 10:
            cancelar_promo_todos()
        elif opcao == 11:
            id = int(input("ID do filme: "))
            deletar_filme(id)
        elif opcao == 12:
            iniciar_arquivos()
        #sair
        elif opcao == 0:
            print("Até logo!")
            break
        else:
            print("Opção inválido!")

menu()