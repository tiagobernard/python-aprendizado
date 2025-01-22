import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# Para rodar o app, no terminal, digite: streamlit run projeto.py

# Carregando os dados
df = pd.read_csv("toalhas.csv")

# Treinando o modelo de regressão linear
modelo = LinearRegression()
x = df[["quantidade"]]
y = df[["custo"]]
modelo.fit(x, y)

# Título e layout da interface
st.title("Prevendo o valor de produção de toalhas premium.")
st.divider()

# Entrada para o diâmetro da pizza
quantidade = st.number_input("Digite a quantidade de toalhas:", min_value=0) #, step=0.5)

# Botão para calcular o preço
if st.button("Calcular preço"):
    if quantidade > 0:
        preco_previsto = modelo.predict([[quantidade]])[0][0]
        plural = "toalha" if quantidade == 1 else "toalhas"
        preco_formatado = f"{preco_previsto:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        st.write(f"O valor de {quantidade:.0f} {plural} é de R${preco_formatado:}.")
        st.balloons()
    if quantidade == 0:
        st.error("Por favor, insira um número maior que zero para o orçamento.")
