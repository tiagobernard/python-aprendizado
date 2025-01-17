# Tela inicial
    #botão inicia chat
        #Quando clicar no botao, vai abrir um popup
    #Titulo
        #Bem vindo ao chat
        #Caixa de Texto, escreva seu nome
        #botao entrar no chat
            #quando clicar no botao
                #sumir com o botao
                #carregar o char
                #carregar o campo de enviar a mensagem
                #enviar a mensagem
                #limpar a caixa de mensagem
#Instalou o Flet - python3 -m pip install flet
#importar o flet
#executar essa função no flet
import flet as ft
#criar uma função para rodar o aplicativo
def main(pagina):
    #colocar o que a função vai fazer
    #titulo
    titulo = ft.Text("HashZap")
    chat = ft.Column()

    #websocket - tunel de comunicação entre 2 usuarios

    def enviar_mensagem_tunel(mensagem):
        #executar tudso o q eu quero que aconteça para todos os usuarios que receberem a mensagem
        #texto = ft.Text(mensagem)
        chat.controls.append(mensagem)
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)
    

    def enviar_mensagem(evento):
        nome_usuario = caixa_nome.value
        texto_campo_mensagem = campo_enviar_mensagem.value
        mensagem = ft.Text(f"{nome_usuario}: {texto_campo_mensagem}")
        pagina.pubsub.send_all(mensagem)
        campo_enviar_mensagem.value = ""
        pagina.update()

    campo_enviar_mensagem = ft.TextField(label="Digite aqui a mensagem")
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    linha_enviar = ft.Row([campo_enviar_mensagem,botao_enviar])

    def entrar_chat(evento):
        #fechar popup
        popup.open = False
        #sumir com o titulo
        pagina.remove(titulo)
        # remove o botao iniciar chat
        pagina.remove(botao)
        #add chat
        pagina.add(chat)
        #adiciona campo de texto enviar mensagem
        pagina.add(linha_enviar)
        #adicionar mensagem que o usuario entrou no chat
        nome_usuario = caixa_nome.value
        mensagem = ft.Text(f"{nome_usuario} entrou no chat.")
        pagina.pubsub.send_all(mensagem)
        pagina.update()

    #criar o popup
    titulo_popup = ft.Text("Bem vindo ao HashZap")
    caixa_nome = ft.TextField(label="Digite seu nome")
    botao_popup = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)
    popup = ft.AlertDialog(title=titulo_popup, content=caixa_nome,actions=[botao_popup])
    
    #botao inicial
    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    botao = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)

    #colocar elementos na página
    pagina.add(titulo)
    pagina.add(botao)
#executar essa função no flet
ft.app(main, view=ft.WEB_BROWSER)