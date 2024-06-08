import flet as ft
from tools import *
from inventory import *
from time import sleep 
from data import *

def vendas_container(page):
    global alfa_TextField, int_TextField, txt_salvos, txt_erros, almoxarifado, float_TextField

    def vender_produto(e=None):
        nome = alfa_TextField.value
        if nome not in almoxarifado or nome == 'Nome' or not nome:
            txt_erros.visible = True
            page.update()
            sleep(1)
            txt_erros.visible = False
            page.update()
            return 

        quantidade = int_TextField.value
        quantidade_real = int(quantidade)
        if not quantidade or quantidade_real == 0 or almoxarifado[nome] < 0:
            txt_erros.visible = True
            page.update()
            return
        
        preco = float_TextField.value
        preco_real = verificar(preco)
        if not float_TextField or preco_real == 0:
            txt_erros.visible = True
            page.update()
            return
        
        processamento_vendas(nome, quantidade_real, preco_real)
        

        txt_salvos.visible = True
        page.update()
        sleep(1)
        txt_salvos.visible = False
        alfa_TextField.value = ""
        int_TextField.value = ""
        float_TextField.value = ""
        page.update()

    botao_add = ft.TextButton(
        text="Vender",
        icon=ft.icons.ADD_OUTLINED,
        icon_color=ft.colors.WHITE,
        style=ft.ButtonStyle(
            color=ft.colors.WHITE,
            bgcolor=ft.colors.GREEN,
            overlay_color=ft.colors.GREEN_900,
            shape=ft.RoundedRectangleBorder(radius=0)
        ),
        scale=0.7,
        on_click=vender_produto
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

def processamento_vendas(nome, quantidade, preco):
    id_venda = 1 if len(vendas) == 0 else len(vendas) + 1
    venda_unidade = [
        nome,
        quantidade,
        preco
    ]
    if data not in vendas:
        vendas[data] = {}
    vendas[data][id_venda] = venda_unidade
    save_data("arquivo_vendas.dat", vendas)