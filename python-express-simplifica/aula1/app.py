#Lógica do nosso programa
# passo 01: importar as bibliotecas
#passo 02: ler os dados dos alunos do arquivo .csv
#passo 03: inserir as informações que estarão no certificado
#passo 04: editar o PDF e ler cada linha do arquivo adicionando nas posições adequadas
#passo 05: salvar os PDFs
#passo 06: rodar o programa

import pandas as pd
from fpdf import FPDF

dados = pd.read_csv("dados.csv")
print(dados['email'])

#Dados do certificado
titulo = "CERTIFICADO DE PARTICIPAÇÃO"
subtitulo = "Este certificado comprova que"
#nome = "Tiago Bernardes"
texto2 = "concluiu com êxito o curso GRATUITO DE PYTHON ministrado por"
texto3 = "Prof. Sauer entre 27/01/2025 a 30/01/2025,"
texto4 = "com carga horária de aproximadamente 8 horas"

#Configurando o PDF
for nomecompleto in dados['nomecompleto']:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", size=15)
    pdf.image("template.png", x=0,y=0)
    pdf.set_text_color(33,24,136)

    pdf.text(65,95, titulo)
    pdf.text(67,120, subtitulo)
    pdf.text(70,145, nomecompleto)
    pdf.text(20,165, texto2)
    pdf.text(50,175, texto3)
    pdf.text(50,185,texto4 )

    pdf.output(f"certificado_{nomecompleto}.pdf")