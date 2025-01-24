#As funções são blocos de código reutilizáveis que nos permitem encapsular tarefas específicas e executá-las quando necessário. As funções nos ajudam a organizar nosso código, evitar a repetição e fazer com que nossos programas sejam mais modulares e fáceis de manter.

def saudacao():
    print("Olá Mundo")
saudacao()

#Parâmetros e argumentos
def saudacaos(nome):
    print(f"Olá, {nome}")
saudacaos("João")
saudacaos("Maria")

#Valores de retorno
def soma(a,b):
    return a + b
resultado = soma(3,4)
print(resultado)

#Funções anônimas (lambda)
quadrado = lambda x: x ** 2
print(quadrado(5))  # Imprime 25

#Escopo das variáveis (local vs. global)
#As variáveis definidas dentro de uma função têm um escopo local, o que significa que só são acessíveis dentro da função. Por outro lado, as variáveis definidas fora de qualquer função têm um escopo global e podem ser acessadas de qualquer parte do programa.

def funcao():
    variavel_local = 10
    print(variavel_local)  # Acessível dentro da função
variavel_global = 20

def funcao2():
    print(variavel_global)  # Acessível de qualquer lugar

funcao()  # Imprime 10
funcao2()  # Imprime 20
print(variavel_global)  # Imprime 20
#print(variavel_local)  # Gera um erro, a variável não está definida neste escopo.

#Funções definidas pelo usuário
def calcular_media(*numeros):
    soma = sum(numeros)
    quantidade = len(numeros)
    media = soma / quantidade
    return media
print("Media:", calcular_media(10,20,30,40))

def somar_3(x):
    return x + 3
somar = lambda x: x + 3
print("Somar a um número", somar(5))

#Documentação de funções (docstrings)
def area_retangulo(base, altura):
    """
    Calcula a área de um retângulo.
    Args:
        base (float): A base do retângulo.
        altura (float): A altura do retângulo.
    Returns:
        float: A área do retângulo.
    """
    return base * altura

#Funções com número variável de argumentos
def soma_variavel(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

print(soma_variavel(1, 2, 3))  # Imprime 6
print(soma_variavel(4, 5, 6, 7))  # Imprime 22