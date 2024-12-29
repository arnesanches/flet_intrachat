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

    # Função para enviar uma mensagem
    def enviar_mensagem(evento):
        texto = f"{campo_nome_usuario.value}: {texto_mensagem.value}"  # Formata a mensagem
        pagina.pubsub.send_all(texto)  # Envia a mensagem para todos os inscritos
        texto_mensagem.value = ""  # Limpa o campo de texto
        pagina.update()  # Atualiza a interface

    # Campo para digitar mensagens
    texto_mensagem = ft.TextField(label="Digite sua mensagem:", on_submit=enviar_mensagem,
                                   bgcolor="#FFFFFF", border_color="#BDC3C7", color="#000000")
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem,  # Botão para enviar mensagem
                                      bgcolor="#2980B9", color="white")  # Azul corporativo

    chat = ft.Column(scroll="always")  # Contêiner das mensagens com scroll habilitado
    linha_mensagem = ft.Row([texto_mensagem, botao_enviar])  # Combinação do campo e botão "Enviar"

    # Função para entrar no chat
    def entrar_chat(evento):
        pagina.remove(titulo)  # Remove o título inicial
        pagina.remove(botao_iniciar)  # Remove o botão inicial
        janela.open = False  # Fecha o popup
        pagina.add(chat)  # Adiciona o contêiner do chat
        pagina.add(linha_mensagem)  # Adiciona a linha com o campo de texto e botão
        texto_entrou_chat = f"{campo_nome_usuario.value} entrou no chat"  # Mensagem de entrada
        pagina.pubsub.send_all(texto_entrou_chat)  # Notifica os participantes
        pagina.update()  # Atualiza a interface

    # Campo para o usuário digitar o nome antes de entrar no chat
    campo_nome_usuario = ft.TextField(label="Escreva seu nome no chat:", on_submit=entrar_chat,
                                       bgcolor="#FFFFFF", border_color="#BDC3C7", color="#000000")
    botao_entrar = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat,  # Botão para entrar no chat
                                      bgcolor="#2980B9", color="white")  # Azul corporativo

    # Janela modal para capturar o nome do usuário
    janela = ft.AlertDialog(title=titulo_janela, content=campo_nome_usuario, actions=[botao_entrar])

    # Função para abrir o popup inicial
    def abrir_popup(evento):
        pagina.dialog = janela  # Define o popup como o diálogo ativo
        janela.open = True  # Abre o popup
        pagina.update()  # Atualiza a interface

    # Botão inicial para abrir o popup de entrada
    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup,
                                       bgcolor="#2980B9", color="white")  # Azul corporativo

    # Adiciona o título e botão inicial à página
    pagina.add(titulo, botao_iniciar)

# Executa o app no navegador
ft.app(main, view=ft.WEB_BROWSER)
