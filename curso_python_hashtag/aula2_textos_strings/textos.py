email = " EMAIL_FALSO@gmail.com "
email = email.lower() #colocar em letra minúscula
email = email.strip() # retirar espaços
print(email)

#tamanho
print(len(email))

#posições
#qual posição está o @?
posicao = email.find("@")
print(posicao)

#pegar pedaços do texto
servidor = email[posicao+1:]
print(servidor)

#trocar pedaço do texto
novo_email = email.replace("gmail.com", "yahoo.com.br") #o terceiro argumento é a quantidade de vezes que vai repetir o replace.
print(novo_email)

#Letras e maiúsculas
nome = "tiago bernardes"
nome = nome.capitalize() #coloca a primeira letra da primeira palavra maiúscula
nome = nome.title() #coloca todas primeiras letras em maiúsculas
print(nome)
nome = nome.upper()
print(nome)

#formatação numérica
faturamento = 1000000
custo = 600
lucro = faturamento - custo
margem = lucro / faturamento
texto = f"O lucro foi de: {lucro:_.2f} e o faturamento foi de: {faturamento:_.2f} e a margem foi de {margem:.0%}"
texto_novo = texto.replace(".",",").replace("_",".")
print(texto_novo)

#exercício
nome2 = "tiago bernardes sabino gomes"
email2 = "tiago@lab82.dev"

# descubra o servidor o email
posicao2 = email2.find("@")
servidor2 = email2[posicao2+1:]
print(servidor2)
# primeiro nome do usuário
posicao_espaco = nome2.find(" ")
primeiro_nome = nome2[:posicao_espaco]
primeiro_nome = primeiro_nome.capitalize()
print(primeiro_nome)
#criar uma mensagem personalizada: "O usuário tal(primeiro nome) foi cadastrado com sucesso com o email tal"
mensagem_personalizada = f"O usuário {primeiro_nome} foi cadastrado com sucesso com o o email {email2}"
print(mensagem_personalizada)