###
#Criar um inventário do harry potter
# inventario = []
# def mostrar_inventario():
#    print("Acessando iventário... - Harry Potter")
#    if not inventario:
#        print ("Está vazia")
#    else:
#        for item in inventario:
#            print(f"{item}")
#    print()

#def adicionar_item():
#    item = input("Digite um item para adicionar ao seu iventário: ")
#    inventario.append(item)
#    print("Este item foi adicionado no seu iventário")
    

#def remover_item():
#    item = input("Digite o nome do item para remover: ")
#    if item in inventario:
#        inventario.remove(item)
#        print(f"{item} foi removido do inventário.")
#    else:
#        print(f"{item} não está no inventário.")



#adicionar_item()
#mostrar_inventario()
#remover_item()
#mostrar_inventario()

# Inventário Harry Potter com menu simples (sem quantidades)

inventario = {}

def mostrar_inventario():
    print("\n📦 Seu inventário:")
    if not inventario:
        print(" - Inventário vazio.")
    else:
        for item in inventario:
            print(f" - {item}")
    print()

def adicionar_itens():
    itens = input("Digite os itens para adicionar (separe por vírgula): ")
    lista_itens = [item.strip() for item in itens.split(",")]
    for item in lista_itens:
        inventario[item] = True
        print(f"{item} foi adicionado ao inventário.")

def remover_itens():
    itens = input("Digite os itens para remover (separe por vírgula): ")
    lista_itens = [item.strip() for item in itens.split(",")]
    for item in lista_itens:
        if item in inventario:
            del inventario[item]
            print(f"{item} foi removido do inventário.")
        else:
            print(f"{item} não está no inventário.")

def menu():
    while True:
        print("\n🔮 MENU DO INVENTÁRIO - Harry Potter")
        print("1. Ver inventário")
        print("2. Adicionar itens")
        print("3. Remover itens")
        print("4. Sair")
        
        escolha = input("Escolha uma opção (1-4): ")

        if escolha == "1":
            mostrar_inventario()
        elif escolha == "2":
            adicionar_itens()
        elif escolha == "3":
            remover_itens()
        elif escolha == "4":
            print("Saindo do inventário. Até mais, bruxo(a)!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Iniciar o programa
menu()

