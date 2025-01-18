class Dez:
    def __init__(self,numero:int):
        self.numero = numero

    def numeral(self):
        if self.numero > 5:
            print("Numero é maior que 5")
        else:
            print("Numero é menor que cinco")

num = Dez(2)
num.numeral()

# Operadores de comparaçao
# == igual
# != diferente de
# > maior que
# < meno que 
# >= maior ou ogual que
# <= menor ou igual que

idade = 18
if idade == 18:
    print("tem exatamente 18 anos")
elif idade != 20: #se colocar if, também vai retornar que não tem 20 anos
    print("Não tem 20 anos")
