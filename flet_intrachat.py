import flet as ft 

def main(pagina):
    # Configurações gerais da página
    pagina.bgcolor = "#D6EAF8"  # Fundo azul claro
    pagina.theme_mode = ft.ThemeMode.LIGHT  # Tema claro

    # Títulos e mensagens
    titulo = ft.Text("Flet IntraChat", size=30, color="#2980B9", weight="bold")  # Título principal
    titulo_janela = ft.Text("Bem-vindo(a) ao Flet IntraChat!", color="#2980B9", weight="bold")  # Texto do popup inicial
