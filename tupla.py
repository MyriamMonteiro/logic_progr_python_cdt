##tuplas - meses do ano

print("Descubra sua cor da sorte de acordo com seu mês")

print("\n Veja o menu a seguir: ")
print("1 - Adicione o mês do seu aniversário")
print("2 - Mostrar sua cor da sorte de acordo com seu mês")
#o sistema não condiz com o remover. Apertando na opção 1,
# já libera automaticamente para selecionar uma próxima opção
#print("3 - Remova o mês selecionado") 
print("4 - Sair")

meses = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho",
        "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")
        
cor_da_sorte = ("Azul escuro", "Roxo", "Verde Água", "Vermelho", "Rosa Claro", "Amarelo",
        "Prata", "Dourado", "Verde musgo", "Azul Claro", "Preto", "Laranja")

while True:
    opcao = input("Digite a opção de 1 a 4: ")
    
    if opcao == "1":
        mes = int(input ("Digite o número do seu mês de nascimento (1-12): "))
        print (f"Foi adicionado seu mês no sitema")
    
    elif opcao == "2":
        if 1 <= mes <= 12:
            seu_mes = meses[mes - 1]
            cor = cor_da_sorte[mes - 1]
            
            print(f"\nVocê nasceu em {seu_mes}.")
            print(f"Sua cor da sorte referente ao seu mês é: {cor}")
        else:
            print("Número de mês inválido!")
#    elif opcao == "3":
#        remove_mes = int(input("Qual é o número do mês que deseja remover? "))
#        if mes in remove_mes:
#            remove_mes.remove(1)
#            print("Foi removido. Agora, você poderá escolher um novo mês")
#        else:
#            print("Erro. Digite o mês digitado anteriormente")
        
    elif opcao == "4":
        print ("Encerrando programa.")
        break
    else:
        print("opção inválida.")