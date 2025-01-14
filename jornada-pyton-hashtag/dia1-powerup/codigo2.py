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
time.sleep(5)
pyautogui.click(x=179, y=87)

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")