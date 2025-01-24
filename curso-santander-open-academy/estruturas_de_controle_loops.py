#FOR
frutas = ["maçã", "banana","laranja"]
for fruta in frutas:
    print(fruta)
print()
for numero in range (1,6):
    print(numero *2)
print()

#WHILE
contador = 0
while contador < 5:
    print(contador)
    contador += 1
print()
cont = 1
while cont <= 5:
    print(cont * 2)
    cont += 1
print()
#CONTROLE DE LOOPS
#BREAK
conta = 0
while True:
    print(conta)
    conta += 1
    if conta == 5:
        break
print()
#CONTINUE
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
print()

#PASS
for i in range(5):
    pass