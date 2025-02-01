#estrutura de lista
lista_produtos = ["airpod", "iphone", "macbook", "ipad",]
precos = [2000,9000,6000,11000]

#estrutura em dicionario
dic_produtos = {"airpod":2000, "iphone":9000, "macbook":6000, "ipad":11000}

#pegar um elemento
print(dic_produtos["airpod"])

#editar um elemento
dic_produtos["airpod"] = 2500
dic_produtos["iphone"] = dic_produtos["iphone"] * 1.3
print(dic_produtos)

#quantidade de itens

print(len(dic_produtos))

#retirar um item do dicionario
dic_produtos.pop("iphone")
print(dic_produtos)

#adicionar um item no dicionario
dic_produtos["apple watch"] = 2500
print(dic_produtos)

#verificar se um produto existe / sempre procura nas chaves do dicionário
if "iphone" in dic_produtos:
    print("O produto existe")
else:
    print("O produto não existe")
#verificar se uma chave existe no dicionário

#verificar se um valor existe nos valores do dicionário
if 9000 in dic_produtos.values():
    print("O valor existe")
else:
    print("O valor não existe")

#exercício
nome_produto = input("Digite o nome do produto: ")
preco_produto = input("Digite o preço do produto: ")

#cadastrar o novo produto (se o produto não existir)
#caso o produto exista, ele vai atualizar o produto
nome_produto = nome_produto.lower()
preco_produto = float(preco_produto)

dic_produtos[nome_produto] = preco_produto
print(dic_produtos)

#o programa tem que no final atualizar o preço de todos os produtos em 10%
produto = "airpod"
#novo_preco = dic_produtos[produto] * 1.1
#print(novo_preco)
#dic_produtos[produto] = novo_preco
#print(dic_produtos)

for produto in dic_produtos:
    novo_preco = dic_produtos[produto] * 1.1
    dic_produtos[produto] = novo_preco
print(dic_produtos)