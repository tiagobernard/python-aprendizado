#IF
idade = 18
if idade >= 18:
   print ("Você é maior de idade.")

#IF-ELSE
idade = 15
if idade >= 18:
   print ("Você é maior de idade.")
else:
   print ("Você é menor de idade.")

#IF-ELIF-ELSE
nota = 85
if nota >= 90:
   print ("Excelente")
elif nota >= 80:
   print ("Muito bom")
elif nota >= 70:
   print ("Bom")
else:
   print ("Precisa melhorar")

idade2 = 20
if idade2 < 18:
   print("É menor de idade")
elif idade2 >= 18 and idade2 < 60:
   print("É um adulto")
elif idade2 > 15:
   print("Maior de 15 anos")
elif idade2 == 60:
   print("Feliz 60 anos")
else:
   print("É um idoso")