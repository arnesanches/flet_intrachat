import flet as ft 

def main(pagina):
    # Configurações gerais da página
    pagina.bgcolor = "#D6EAF8"  # Fundo azul claro
    pagina.theme_mode = ft.ThemeMode.LIGHT  # Tema claro

    # Títulos e mensagens
    titulo = ft.Text("Flet IntraChat", size=30, color="#2980B9", weight="bold")  # Título principal
    titulo_janela = ft.Text("Bem-vindo(a) ao Flet IntraChat!", color="#2980B9", weight="bold")  # Texto do popup inicial

    # Função para exibir mensagens no chat ao receber dados pelo canal PubSub
    def enviar_mensagem_tunel(mensagem):
        chat.controls.append(ft.Text(mensagem, color="#34495E"))  # Adiciona mensagem ao chat
        pagina.update()  # Atualiza a interface

    pagina.pubsub.subscribe(enviar_mensagem_tunel)  # Inscreve a função no canal de mensagens

        # Campo para digitar mensagens
    texto_mensagem = ft.TextField(label="Digite sua mensagem:", on_submit=enviar_mensagem,
                                   bgcolor="#FFFFFF", border_color="#BDC3C7", color="#000000")
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem,  # Botão para enviar mensagem
                                      bgcolor="#2980B9", color="white")  # Azul corporativo

    chat = ft.Column(scroll="always")  # Contêiner das mensagens com scroll habilitado
    linha_mensagem = ft.Row([texto_mensagem, botao_enviar])  # Combinação do campo e botão "Enviar"

