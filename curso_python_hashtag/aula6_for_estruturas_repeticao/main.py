for i in range(10):
    print(i)
    print("Se inscreva no canal")

lista_preco = [1500, 1000, 800, 2000]
taxa_imposto = 0.3

for preco in lista_preco:
    imposto = preco * taxa_imposto
    print(f"Preço do produto {preco} e imposto é de {imposto}")

#exemplos
#produtos de até 1000 reais pagam 10%
#produtos acima de 1000 reais pagam 15%

for preco in lista_preco:
    if preco <= 1000:
        taxa = 0.15
    else:
        taxa = 0.15
    imposto = taxa * preco
    print(f"O Preço do produto {preco} e imposto é de {imposto}")

#exemplo 2
#mesma regra de imposto, mas agora calcular o imposto somado com o preço do produto
print("===========")
total_imposto = 0
for preco in lista_preco:
    if preco > 1000:
        taxa = 0.15
    else:
        taxa = 0.10
    imposto = preco * taxa
    total_imposto = total_imposto + imposto
    print(f"Preço do produto {preco} e imposto é de {imposto}")

print(f"Total de imposto é de {total_imposto}")

#exemplo 3

vendas_23 = {"jan": 15000, "fev": 10000, "mar": 5000}
vendas_24 = {"jan": 16000, "fev": 11000, "mar": 5100}

# calculo percentual de crescimento
# 16000 / 15000 - 1 = -> Quantos porcento eu cresci de um ano para outro.
for mes in vendas_24:
    valor_23 = vendas_23[mes]
    valor_24 = vendas_24[mes]
    crescimento = valor_24 / valor_23 - 1
    print(f"O crescimento do mês {mes} foi de {crescimento * 100:.2f}%")