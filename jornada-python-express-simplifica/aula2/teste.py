import pandas as pd

tabela = pd.read_csv("alunos.csv")
print(tabela)

nome = tabela.loc[0, "Nome"]