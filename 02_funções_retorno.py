def soma():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    return num1 + num2

def subtracao():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    return num1 - num2

def multiplicar():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    return num1 * num2

def divisao():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    return num1 / num2

while True:
    escolha = int(input('''
    [1] Somar
    [2] Subtrair
    [3] Multiplicar
    [4] Dividir
    [5] Sair
    Escolha uma opção:  '''))

    if escolha == 1:
        print(soma())
    elif escolha == 2:
        print(subtracao())
    elif escolha == 3:
        print(multiplicar())
    elif escolha == 4:
        print(divisao())
    elif escolha == 5:
        print("Obrigado por usar!")
        break
    else:
        print("Opção inválida. Tente novamente.")
