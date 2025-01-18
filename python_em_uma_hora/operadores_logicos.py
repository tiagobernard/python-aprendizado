# and - verifica se ambas as condiçoes são verdadeira
# or - verifica se pelo meno uma das condições é verdadeira
# not - inverte o valor de uma condiçãoe transforma true em valse e vice-versa

idade = 25
possui_cnh = True
if idade >= 18 and possui_cnh:
    print("pode dirigir")
else:
    print("não pode dirigir")

possui_ingresso = True
if idade >= 18 and possui_ingresso:
    print("Bem vindo ao evento")
elif not possui_ingresso:
    print("Você precisa de um ingresso")
else:
    print("Desculpe, você precisa ser maior de idade para entrar")