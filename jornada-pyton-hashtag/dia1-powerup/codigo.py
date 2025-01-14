#Passo1: Abir o sistema da empresa
#    https://dlp.hashtagtreinamentos.com/python/intensivao/login
#Passo2: Fazer login
#Passo3: Importar a base de dados do produto
#Passo4: Cadastrar 1 produto
#Passo5: Repetir o passo 4 até acabar todos os produtos

import pyautogui
import time


pyautogui.hotkey("command", "space")
pyautogui.write("chrome")
pyautogui.PAUSE = 1 # o comando digitar Chrome vai demorar 1 segundo para ser executado
pyautogui.press("enter")

time.sleep(5)

pyautogui.click(x=949, y=586)
pyautogui.click(x=179, y=87)

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

#email pythonimpressionador@gmail.com
#senha 'minha senha aqui'

#importar base de dados
import pandas

tabela = pandas.read_csv("produtos.csv")

print(tabela)

time.sleep(2)

for linha in tabela.index:
    pyautogui.click(x=657, y=332)

    #codigo
    codigo = tabela.loc(linha,"codigo")
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    #Marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    # tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    #categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    #Preço Unitário
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    #preco de custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    #observação
    obs = tabela.loc[linha, "obs"]
    if obs != "nan":
        pyautogui.write(str(obs))
    pyautogui.press("tab")

    pyautogui.press("enter")

    # numero positivo = scroll para cima
    # numero negativo = scroll para baixo
    pyautogui.scroll(10000) #ou dar um press home
