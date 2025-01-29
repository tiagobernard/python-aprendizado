import pandas as pd
import pyautogui
import time

pyautogui.hotkey("command", "space")
pyautogui.write("opera")
pyautogui.PAUSE = 1 # o comando digitar Chrome vai demorar 1 segundo para ser executado
pyautogui.press("enter")
pyautogui.hotkey("command", "t")
#time.sleep(1)
pyautogui.click(x=2145, y=86)
pyautogui.write("http://www.sauer.pro.br/python/automacao/index.html")
pyautogui.press("enter")
time.sleep(2)
pyautogui.click(x=2560, y=609)

pyautogui.write("admin")
pyautogui.press("tab")
pyautogui.write("SimplificaPython")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(1)

tabela = pd.read_csv("alunos.csv")

for linha in tabela.index:
    pyautogui.click(x=2530, y=399)

    nome = tabela.loc[linha, "Nome"]
    pyautogui.write(nome)
    time.sleep(0.5)
    pyautogui.press("tab")

    email = tabela.loc[linha, "Email"]
    pyautogui.write(email)
    time.sleep(0.5)
    pyautogui.press("tab")

    endereco = tabela.loc[linha, "Endereco"]
    pyautogui.write(endereco)
    time.sleep(0.5)
    pyautogui.press("tab")

    telefone = tabela.loc[linha, "Telefone"]
    pyautogui.write(telefone)
    time.sleep(0.5)
    pyautogui.press("tab")
    
    pyautogui.press("enter")
    pyautogui.scroll(1000)