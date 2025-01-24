#Quando escrevemos programas, é comum nos depararmos com situações inesperadas ou erros durante a execução. Python fornece um mecanismo para lidar com esses erros de maneira controlada utilizando o tratamento de exceções. Isso nos permite capturar e lidar com erros específicos sem que o programa pare abruptamente.

#Erros comuns em Python

#Erro de sintaxe (SyntaxError)
#Erro de nome (NameError)
#Erro de tipo (TypeError)
#Erro de índice (IndexError)

#Manejo de exceções
#TRY
try:
    # Código que pode gerar uma exceção
    resultado = 10 / 0  # Divisão por zero
    print(resultado)
except ZeroDivisionError:
    print("Erro: Divisão por zero")

#EXCEPT
try:
    # Código que pode gerar uma exceção
    resultado = 10 / 0  # Divisão por zero
    print(resultado)
except ZeroDivisionError:
    print("Erro: Divisão por zero")
except ValueError:
    print("Erro: Valor inválido")

#FINALLY
try:
    # Código que pode gerar uma exceção
    arquivo = open("arquivo.txt", "r")
    # Realizar operações com o arquivo
except FileNotFoundError:
    print("Erro: Arquivo não encontrado")
finally:
    arquivo.close()  # Fechar o arquivo sempre, mesmo se ocorrer uma exceção