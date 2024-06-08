import flet as ft
from inventory import *
from tools import *
from data import *


def compras_content(page):
    global alfa_TextField, int_TextField, float_TextField, txt_erros, txt_salvos
    
    def cadastrar_produto(e=None):
        global alfa_TextField, int_TextField, float_TextField, txt_erros, txt_salvos
        nome = alfa_TextField.value
        if nome == 'Nome' or not nome:
            txt_erros.visible = True
            page.update()
            return

        quantidade = int_TextField.value
        if not quantidade or int(quantidade) <= 0:
            txt_erros.visible = True
            page.update()
            return

        preco = float_TextField.value
        if not preco or verificar(preco) <= 0:
            txt_erros.visible = True
            page.update()
            return

        quantidade_real = int(quantidade)
        preco_real = verificar(preco)
        if nome in almoxarifado:
            almoxarifado[nome] += quantidade_real
        else:
            almoxarifado[nome] = quantidade_real
        save_data("arquivo_almoxarifado.dat", almoxarifado)
        processamento_relatorio(nome, quantidade, preco_real)

        txt_salvos.visible = True
        txt_erros.visible = False
        alfa_TextField.value = ""
        int_TextField.value = ""
        float_TextField.value = ""

        page.update()

        sleep(2)
        txt_salvos.visible = False
        alfa_TextField.value = ""
        int_TextField.value = ""
        float_TextField.value = ""

        page.update()

    botao_add = ft.TextButton(
        text="Adicionar",
        icon=ft.icons.ADD_OUTLINED,
        icon_color=ft.colors.WHITE,
        style=ft.ButtonStyle(
            color=ft.colors.WHITE,
            bgcolor=ft.colors.GREEN,
            overlay_color=ft.colors.GREEN_900,
            shape=ft.RoundedRectangleBorder(radius=0)
        ),
        scale=0.7,
        on_click=cadastrar_produto
    )

    content = ft.Column(
        controls=[
            alfa_TextField,
            int_TextField,
            float_TextField,
            botao_add,
            txt_salvos,
            txt_erros
        ], 
        expand=True,
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
    )
    return content

def processamento_relatorio(nome, quantidade, preco):
    """
    Processa o relatório de compras, adicionando a entrada do ingrediente.

    Args:
        nome (str): Nome do ingrediente.
        quantidade (int): Quantidade do ingrediente.
        preco (float): Preço do ingrediente.
    """
    hora = datetime.now().strftime("%H:%M:%S")

    entrada_relatorio = {
        "Hora": hora,
        "Nome": nome,
        "Quantidade": quantidade,
        "R$": preco
    }

    if data not in compras:
        compras[data] = []
    compras[data].append(entrada_relatorio)

    # Salvar o relatório atualizado
    save_data("arquivo_relatorio_compras.dat", compras)