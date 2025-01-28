faturamento = 1000
custo = 600
lucro = faturamento - custo

if lucro >= 0 :#condição / comparação
    print("Lucro de:", lucro)
else:
    print("Prejuízo de:", lucro)

print("Acabou")

#Exemplo 1

produtos = ["ipod", "imac", "iphone"]
#novo_produto = input("Digite o nome do produto: ")
novo_produto = "macbook"
if novo_produto in produtos:
    print("Produto já existente")
else: 
    print(f"{novo_produto} cadastrado com sucesso")
    produtos.append(novo_produto)

print(produtos)

#Exemplo 2
#bonus funcionarios
#vendas maiores do que 15000, então ele ganha 500 de bonus
#se as vendas forem entre 5000 e 15000, então ele ganha 100 de bonus
#se as vendas forem menores do que 5000 então ele não ganha bonus
vendas = 20000
if vendas >= 15000:
    bonus = 500
else:
    if vendas >= 5000:
        bonus = 100
    else:
        bonus = 0

print(f"O bonus do funcionário: {bonus}")

if vendas >= 15000:
    bonus = 500
elif vendas >= 5000:
    bonus = 100
else:
    bonus = 0

print(f"O bonus do funcionário: {bonus}")

#Exemplo 3
#bonus funcionarios
#vendas maiores do que 15000, então ele ganha 500 de bonus
#se as vendas forem entre 5000 e 15000, então ele ganha 100 de bonus
#se as vendas forem menores do que 5000 então ele não ganha bonus
#só ganha bonus se as vendas totais da empresa forem maior do que 1000

vendas_empresa = 200000
meta_empresa = 100000
vendas_funcionario = 11000

if vendas_funcionario >= 15000 and vendas_empresa >= meta_empresa:
    bonus = 500
elif vendas_funcionario >= 5000 and vendas_empresa >= meta_empresa:
    bonus = 100
else:
    bonus = 0

print(f"O bonus do funcionário: {bonus}")