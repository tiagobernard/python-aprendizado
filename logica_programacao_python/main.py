"""
cometário em várias linhas

"""

nome = input("Digite seu nomme: ")
if nome == "Tiago":
    print("O nome é verdadeiro")
    idade = input("Qual é a idade: ")
    if idade == str(42):
        print("Nome e idade corretos")
    else:
        print("O nome foi verdadeiro e a idade foi falsa")

# Shift tab tira a identação

nomes = ["Tiago", "João"]
print(nomes)

nomeTemporario = input("Digite mais algum nome: ")
nomes.append(nomeTemporario)
print(nomes)
for nome in nomes:
    print(nome)