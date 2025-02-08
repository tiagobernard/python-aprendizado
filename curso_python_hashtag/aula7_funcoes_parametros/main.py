lista_precos = [1500, 2300, 5000, 1000, 2000]

def definir_taxa_imposto(preco):
    if preco > 1500:
        taxa = 0.2
    elif preco > 1000:
        taxa = 0.15
    else:
        taxa = 0.10
    return taxa

def calcular_imposto(lista_valores):
    imposto_total = 0
    for preco in lista_valores:
        taxa_imposto = definir_taxa_imposto(preco)
        imposto = preco * taxa_imposto
        imposto_total = imposto_total + imposto
    return imposto_total

imposto_lista1 = calcular_imposto(lista_precos)
print(imposto_lista1)

lista2_precos = [1500, 2300, 5000, 1000]
imposto_lista2 = calcular_imposto(lista2_precos)
print(imposto_lista2)

def se_inscreve_canal():
    print("Inscreva-se no canal!")

se_inscreve_canal()

