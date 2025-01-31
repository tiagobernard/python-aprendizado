lista_produtos = ["ipad", "iphone", "airpod"]
lista_precos = [7000, 5000, 2000]

dic_produtos = {"ipad" : 7000, "iphone" : 5000, "airpod" : 2000}

#pegar um item
produto = "iphone"
posicao = lista_produtos.index(produto)
preco = lista_precos[posicao]
print(produto,preco)


print(dic_produtos["iphone"])

dic_vendas = { "Lira": [1000,500,1500], "João" : [500,400,500]}
print(dic_vendas["Lira"])


#editar um item
dic_produtos["iphone"] = dic_produtos["iphone"] * 1.1
print(dic_produtos)

#adicionar um item
dic_produtos["macbook"] = 12000
print(dic_produtos)

#remover um item
item_removido = dic_produtos.pop("macbook") #retorna o item removido
print(item_removido)
print(dic_produtos)

#verificar se existe um item no dicionario
print("macbook" in dic_produtos)
print("iphone" in dic_produtos.keys())
print(2000 in dic_produtos.values())

produtos = list(dic_produtos.keys())
print(produtos)
precos = list(dic_produtos.values())
print(precos)

# contagem de itens no dicionario
qtde = len(dic_produtos)
print(qtde)


#exercício
dic_produtos = {"ipad" : 7000, "iphone" : 5000, "airpod" : 2000, "macbook" : 12000}

produto_buscado = input("Digite o produto que deseja buscar: ")
produto_buscado = produto_buscado.lower()
produto_buscado = produto_buscado.strip()
if produto_buscado in dic_produtos:
    preco = dic_produtos[produto_buscado]
    print(f"{produto_buscado} encontrado\nPreço: {preco}")
else:
    print(f"{produto_buscado} não encontrado na base de dados")