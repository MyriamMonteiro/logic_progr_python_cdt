##MVC
#Model
### Operação aritimética
### main

#View
### impressão do resultado
### mostrar_menu

#Controller
### input - entrada do usuário
### print - sáida do resultado
### obter_numeros

def mostrar_menu():
    print("\nCalculadora")
    print("1. Adição")
    print("2. Subtração")
    print("5. Sair")
    print("---------------")

def obter_numeros():
    while True:
        try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
        return num1, num2
    except ValueError:
    print("Entrada iválida. Por favor, digite números válidos.")

def main():
    while True:
        mostrar-menu()
        opcao = input
