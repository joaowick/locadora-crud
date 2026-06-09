# Atividade João Torres Moreira - Bootcamp Porto
#main.py

from filmes import(
    iniciar_arquivos,
    listar_filmes,
    cadastrar_filme,
    pesquisar_filme,
    alterar_preco,
    adicionar_estoque,
    promocao_filme,
    promocao_todos,
    cancelar_promo_filme,
    cancelar_promo_todos,
    deletar_filme,
    buscar_filme_por_id
)
from vendas import(
    registrar_venda
)

from relatorios import(
    painel_bi,
    listar_historico
)

def menu():
    while True:
        print("\n=== LOCADORA DE FILMES ===")
        print("01 - Listar filmes")
        print("02 - Cadastrar filmes")
        print("03 - Pesquisar filme")
        print("04 - Alterar preço")
        print("05 - Adicionar estoque")
        print("06 - Registrar venda")
        print("07 - Aplicar promoção")
        print("08 - Cancelar promoção")
        print("09 - Deletar de um filme")
        print("10 - Iniciar os arquivos")
        print("11 - Painel de Business")
        print("12 - Histórico de mais vendidos")
        print("0 - Sair")
    
        try:
            opcao = int(input("\nEscolha uma opção: "))
        except ValueError:
            print(f"Opção inválida! Digite apenas número.")
            continue
    

        # 01 - Listar filmes
        if opcao == 1:
            listar_filmes()
        # 02 - Cadastrar filmes
        elif opcao == 2:
            try:
                titulo = input("Titulo: ")
                diretor = input("Diretor: ")
                ano = int(input("Ano: "))
                genero = input("Genero: ")
                preco = float(input("Preço: "))
                estoque = int(input("Estoque: "))
                cadastrar_filme(titulo, diretor, ano, genero, preco, estoque)
            except ValueError:
                print("Somente número")
        # 03 - Pesquisar filme
        elif opcao == 3:
            print("Pesquisar categoria por: 1 - Titulo | 2 - Diretor | 3 - Ano")
            try:
                sub = int(input("Escolha a categoria: "))
            except ValueError:
                print("Somente número")
                continue
            if sub == 1:
                pesquisar_filme("titulo", input("Titulo: "))
            elif sub == 2:
                pesquisar_filme("diretor", input("Diretor: "))
            elif sub == 3:
                pesquisar_filme("ano", input("Ano: "))
        # 04 - Alterar preço        
        elif opcao == 4:
            try:
                id = int(input("ID do filme: "))
                filme = buscar_filme_por_id(id)

                if not filme:
                    print('Filme não encontrado')
                else:
                    print(f"Preço atual do filme '{filme['titulo']}' é de R$ {filme['preco']:.2f}")
                    preco = float(input("Novo preço: R$ "))
                    alterar_preco(id, preco)
            except ValueError:
                print("Digite apenas números!")
        # 05 - Adicionar estoque
        elif opcao == 5:
            try:
                id = int(input("ID do filme: "))
                filme = buscar_filme_por_id(id)
                
                if not filme:
                    print(f"ID {id} não encontrado")
                else:
                    print(f"O estoque atual do filme '{filme['titulo']}' é {filme['estoque']}.")
                    quantidade = int(input("Quantos devo adicionar: "))
                    adicionar_estoque(id, quantidade)
            except ValueError:
                print("Somente número")
        # 06 - Registrar venda
        elif opcao == 6:
            try:
                id = int(input("ID do filme: "))
                quantidade = int(input("Quantidade: "))
                registrar_venda(id, quantidade)
            except ValueError:
                print("Somente os números.")
        # 07 - Aplicar promoção
        elif opcao == 7:
            try:
                tipo_promo = int(input("Qual tipo de promo? 1 - Um filme | 2 - Todos os filmes: "))
                if tipo_promo == 1:
                    id = int(input("ID do filme: "))
                    desconto = float(input("Desconto (%): "))
                    promocao_filme(id, desconto)
                elif tipo_promo == 2:
                    desconto = float(input("Desconto (%): "))
                    promocao_todos(desconto)
                else:
                    print(f"{id} inválido!")
            except ValueError:
                print("Somente os números.")
        # 08 - Cancelar promoção
        elif opcao == 8:
            try:
                tipo_cancelamento = int(input("Qual forma de cancelamento? 1 - Um filme | 2 - Todos os filmes: "))
                if tipo_cancelamento == 1:
                    id = int(input("ID do filme: "))
                    cancelar_promo_filme(id)
                elif tipo_cancelamento == 2:
                    cancelar_promo_todos()
                else:
                    print(f"{tipo_cancelamento} é inválido!")
            except ValueError:
                print("Somente os números.")
        # 09 - Deletar de um filme
        elif opcao == 9:
            try:
                id = int(input("ID do filme: "))
                deletar_filme(id)
            except ValueError:
                print("Somente os números.")
        # 10 - Iniciar os arquivos
        elif opcao == 10:
            iniciar_arquivos()
        # 11 - Painel de BI
        elif opcao == 11:
            painel_bi()
        # 12 - Lista de histórico
        elif opcao == 12:
            listar_historico()
        #sair
        elif opcao == 0:
            print("Até logo!")
            break
        else:
            print("Opção inválido!")

menu()