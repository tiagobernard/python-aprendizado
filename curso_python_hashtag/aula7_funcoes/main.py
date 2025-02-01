lista_precos = [1500,1000,800,3000]

#imposto
#aliquota 1 = IR = 0.2, se o preço do produto for até 2000, acima disso a aliquota é 0.3
#aliquota 2 = ICMS = 0.15
#aliquota 3 = CSLL = 0.05

def calcula_imposto_total(preco):
    if preco <= 2000:
        imposto_ir = 0.2 * preco
    else:
        imposto_ir = 0.3 * preco
    imposto_icms = 0.15 * preco
    imposto_csll = 0.05 * preco
    imposto_total = imposto_ir + imposto_icms + imposto_csll
    return imposto_total

for preco in lista_precos:
    imposto_total = calcula_imposto_total(preco)
    print(f"O imposto total sobre um produto de R$ {preco} é de {imposto_total}")

nova_lista_precos = [3000, 5000, 6000, 7000]
for preco in nova_lista_precos:
    imposto_total = calcula_imposto_total(preco)
    print(f"O imposto total sobre um produto de R$ {preco} é de {imposto_total}")