#ARITIMÉTICOS
#Soma (+): soma dois valores.
#Subtração (-): subtrai o segundo valor do primeiro.
#Multiplicação (*): multiplica dois valores.
#Divisão (/): divide o primeiro valor pelo segundo e devolve um resultado de tipo flutuante.
#Divisão inteira (//): divide o primeiro valor pelo segundo e devolve um resultado de tipo inteiro (a parte decimal é descartada).
#Módulo (%): devolve o resto da divisão entre o primeiro valor e o segundo.
#Exponenciação (**): eleva o primeiro valor à potência do segundo.

a = 10
b = 3

soma = a + b   # 13
subtracao = a - b    # 7
multiplicacao = a * b    # 30
divisao = a / b   # 3.333333333
divisao_inteira = a // b   # 3
modulo = a % b   # 1
exponenciacao = a ** b   # 1000

#COMPARAÇÃO
#Igual a (==): devolve True se ambos os valores são iguais.
#Diferente de (!=): devolve True se os valores são diferentes.
#Maior que (>): devolve True se o primeiro valor é maior que o segundo.
#Menor que (<): devolve True se o primeiro valor é menor que o segundo.
#Maior ou igual que (>=): devolve True se o primeiro valor é maior ou igual que o segundo.
#Menor ou igual que (<=): devolve True se o primeiro valor é menor ou igual que o segundo.

a = 10
b = 3

igual = a == b   # False
diferente = a != b   # True
maior_que = a > b   # True
menor_que = a < b   # False
maior_ou_igual = a >= b   # True
menor_ou_igual = a <= b   # False

#LÓGICOS
#AND (and): devolve True se ambas as condições são verdadeiras.
#OR (or): devolve True se ao menos uma das condições é verdadeira.
#NOT (not): inverte o valor de uma condição, devolve True se a condição é falsa e False se a condição é verdadeira.

a = 10
b = 3

resultado_and = (a > 5) and (b < 5)   # True
resultado_or = (a > 15) or (b < 5)   # True
resultado_not = not (a > 5)   # False