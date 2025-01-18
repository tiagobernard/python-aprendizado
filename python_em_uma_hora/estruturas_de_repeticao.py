#for - percorre elementos dentro de uma sequencia
for i in range(5):
    print("Repetição numero", i)

frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print("Eu gosto de", fruta)

#while - executa um bloco de código enquando a condição for verdadeira
# É bom para quando não sabemos quantas vezes é preciso repetir a ação
contador = 0
while contador < 5:
    print("Contagem", contador)
    contador += 1

#Break - interrompe uma repetição ao atingir um certo ponto antes que ela termine naturalmente
for numero in range(10):
    if numero == 5:
        break
    print(numero)
print("---------")

#Continue - pula a interção atual e pula para a próxima
for numero in range(10):
    if numero == 6:
        continue
    print(numero)
print("---------")

#repetições aninhadas
for i in range(3):
    for j in range(2):
        print("i:", i, "| j",j )

