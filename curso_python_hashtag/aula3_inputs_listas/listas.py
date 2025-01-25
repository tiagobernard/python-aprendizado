lista_vendas = [100,50,1000,800,35]

print(lista_vendas[0]) #pega o primeiro item da lista, -1 pega o último item da lista.

#tamanho da lista
qtde_vendas = len(lista_vendas)
print(len(lista_vendas)) #conta quantos item tem na lista

#somar os itens da lista
total_de_vendas = sum(lista_vendas)
print(total_de_vendas)

#min, max e media
print(min(lista_vendas))
print(max(lista_vendas))
print(total_de_vendas / qtde_vendas)

# encontrar um elemento na lista (a posição do elemento na lista)
print(1000 in lista_vendas)

lista_produtos = ["iphone", "ipad", "apple watch", "airpod", "macbook"]
print("airpod" in lista_produtos)

posicao = lista_produtos.index("airpod")
print(posicao)

pedaco_lista = lista_produtos[posicao:]
print(pedaco_lista)

# edita um item
lista_precos = [5000,7000,3000,1000,10000]
#novo_preco = lista_precos[0] * 1,1
lista_precos[0] = lista_precos[0] * 1.1
print(lista_precos)

#remover o item da lista - remove e pop
lista_produtos.remove("macbook")
print(lista_produtos)
item_removido = lista_produtos.pop(-2) # remove o item da lista pela sua posição. Esse item pode ser armazenado em uma variável.
print(lista_produtos)
print(item_removido) # o item removido foi armazenado pelo pop

#Adicionar item na lista - append e extend
lista_produtos.append("macbook air")
lista2_produtos = ["PC", "air tag", "caixa de som"]

lista_produtos.extend(lista2_produtos)
print(lista_produtos)

#inserir um item em uma posição específica
lista_produtos.insert(1, "airpod max") #duas informações, uma é a posição, o índice e a outra informação é o item a ser adicionado. Aceita um item que já existe na lista.
print(lista_produtos)

# contar quantas vezes um item apaerece na lista
lista_produtos.insert(2, "airpod")
print(lista_produtos)
print(lista_produtos.count("airpod"))

#ordenar uma lista
lista_produtos.sort() # por padrão o sort organiza por ordem crescente. Se for texto em ordem alfabética ASCII. Letras maiúsculas antes
print(lista_produtos)
lista_precos.sort(reverse=True)
print(lista_precos)