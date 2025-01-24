#Em Python, a entrada e saída de dados nos permite interagir com o usuário e manipular arquivos. Podemos solicitar informações ao usuário, mostrar resultados na tela e ler ou escrever dados em arquivos externos.

#Entrada de dados do usuário
#Para obter informações do usuário durante a execução do programa, podemos utilizar a função input(). Esta função mostra uma mensagem na tela e espera que o usuário insira um valor.

nome = input("Insira seu nome: ")
idade = input("Insira sua idade: ")

print("Olá, " + nome + "!")
print("Você tem " + idade + " anos.")
print()

idade2 = int(input("Insira sua idade: "))
if idade2 >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

#Saída de dados
nome3 = "Juan"
idade3 = 25


print(f"Olá, meu nome é {nome3} e tenho {idade3} anos.")