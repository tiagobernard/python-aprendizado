def soma(a,b):
    return a + b
def subtracao(a,b):
    return a - b
def multiplicacao(a,b):
    return a * b
def divisao(a,b):
    return a / b

def menu():
    print("Selecione a operação")
    print("1. Soma")
    print("2. Subtracao")
    print("3. Multiplicação")
    print("4. Divisão")

def calculadora():
    #continuar = 0
    #while continuar < 1
    #-----
    while True:
        menu()
        escolha = input("Digite o número da operação ou q para sair: ")
        if escolha == "q":
            print("Encerrando a Calculadora. Obrigado!")
            break
        if escolha in ['1','2','3','4']:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        if escolha == '1':
            print("Resultado: ",soma(num1,num2))
        elif escolha == '2':
            print("Resultado: ",subtracao(num1,num2))
        elif escolha == '3':
            print("Resultado: ",multiplicacao(num1,num2))
        elif escolha == '4':
            print("Resultado: ",divisao(num1,num2))
        else:
            print("Digite uma opção entre 1 e 4 ou q para sair")
        #continuar += 1

        continuar = input("Deseja realizar outra operação? s/n: ")
        if continuar.lower() != 's':
            print("Encerrando a calculadora. Obrigado!")
            break
calculadora()