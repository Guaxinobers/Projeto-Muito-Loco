def carregar_estoque(arquivo):

    estoque = {}
    try:

        with open(arquivo, "r") as f:
            for linha in f:

                item, quantidade = linha.strip().split(":")
                estoque[item] = int(quantidade)

    except FileNotFoundError:
        pass  # Se o arquivo não existir, começa com estoque vazio.

    return estoque

def salvar_estoque(arquivo, estoque):

    with open(arquivo, "w") as f:

        for item, quantidade in estoque.items():

            f.write(f"{item}:{quantidade}\n")

def adicionar_item(estoque):

    item = input("Nome do item para adicionar: ")

    quantidade = int(input(f"Quantidade de {item}: "))

    if item in estoque:
        estoque[item] += quantidade

    else:
        estoque[item] = quantidade

    print(f"{quantidade} unidades de {item} adicionadas ao estoque.")

def remover_item(estoque):

    item = input("Nome do item para remover: ")

    if item in estoque:
        quantidade = int(input(f"Quantidade de {item} para remover: "))

        if quantidade >= estoque[item]:

            del estoque[item]
            print(f"{item} foi removido completamente do estoque.")

        else:

            estoque[item] -= quantidade
            print(f"{quantidade} unidades de {item} removidas.")
    else:
        print(f"{item} não está no estoque.")

def mostrar_estoque(estoque):

    if estoque:

        print("\nEstoque atual:")
        for item, quantidade in estoque.items():

            print(f"{item}: {quantidade} unidades")

    else:
        print("\nO estoque está vazio.")

def main():
    
    arquivo_estoque = "estoque.txt"
    estoque = carregar_estoque(arquivo_estoque)

    while True:
        print("\n=== Menu ===")
        print("1. Adicionar item")
        print("2. Remover item")
        print("3. Mostrar estoque")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_item(estoque)

        elif opcao == "2":
            remover_item(estoque)

        elif opcao == "3":
            mostrar_estoque(estoque)

        elif opcao == "4":
            salvar_estoque(arquivo_estoque, estoque)
            print("Estoque salvo. Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()