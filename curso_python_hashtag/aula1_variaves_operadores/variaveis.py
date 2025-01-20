faturamento = 1000
custo = 600
novas_vendas = 1000
faturamento = faturamento + novas_vendas
imposto = 0.15 * faturamento
lucro = faturamento - custo - imposto

print("Faturamento: ", faturamento)
print("Custo: ", custo)
print("Imposto: ", imposto)
print(f"Lucro: {lucro:.2f}")

mensagem = "O faturamento da loja foi de 2000" #string
teve_lucro = True #booleano

'''
TIPOS DE DADOS
números interiros == int
número com casa decimal == float
boolean, booleanos = True ou False
--------
OPERADORES ESPECIAIS
mod -> % - resto da divisão - 10 % 3
floor division -> //
'''

#mod
print(10 % 3) # == 1
print(310 % 12) #resto da divisaos
anos = int(310 / 12) # transfora o float em inteiro
anos2 = round(310/12) #arredontamento matemático, arredonda pra cima ou pra baixo, depende do resultado float
print(anos)
print(anos2)

#floor division
print(310 // 12)