#Em Python, um módulo é um arquivo que contém definições de funções, classes e variáveis que podem ser utilizadas em outros programas. A importação de módulos nos permite acessar a funcionalidade definida em outros arquivos e reutilizar código de maneira eficiente. Além disso, podemos criar nossos próprios módulos para organizar e modularizar nosso código.

import math

resultado = math.sqrt(25)
print(resultado)  # Imprime 5.0

from math import sqrt
resultado = sqrt(25)
print(resultado)  # Imprime 5.0

#Funções e classes de módulos padrão
import random
import datetime
numero_aleatorio = random.randint(1, 10)
print(numero_aleatorio)  # Imprime um número inteiro aleatório entre 1 e 10
data_atual = datetime.datetime.now()
print(data_atual)  # Imprime a data e hora atual

#Criação de módulos próprios
#Criar e utilizar módulos personalizados

import meu_modulo
meu_modulo.saudar("João")  # Imprime "Olá, João!"
resultado = meu_modulo.calcular_soma(5, 3)
print(resultado)  # Imprime 8

#Organização do código em módulos
import operacoes
import utilidades

resultado = operacoes.somar(5, 3)
utilidades.imprimir_mensagem(f"O resultado da soma é: {resultado}")

nome = utilidades.obter_nome_usuario()
utilidades.imprimir_mensagem(f"Olá, {nome}!")