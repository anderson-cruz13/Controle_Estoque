import flet as ft
from data import *
from time import sleep

def almoxarifado_content(page):
    encontrado = ft.Text(value="Item encontrado", color=ft.colors.BLACK, bgcolor=ft.colors.GREEN, weight=ft.FontWeight.BOLD, visible=False, text_align=ft.TextAlign.CENTER)
    nao_encontrado = ft.Text(value="Item não encontrado", color=ft.colors.BLACK, bgcolor=ft.colors.RED, weight=ft.FontWeight.BOLD, visible=False, text_align=ft.TextAlign.CENTER)

    def buscar_almoxarifado(e=None):
        nome = e.control.value
        if nome:
            if nome in almoxarifado:
                exibir.content.controls = [ft.Text(value=f"{nome}: {almoxarifado[nome]} un.", size=15, color=ft.colors.BLACK)]
                encontrado.visible = True
                nao_encontrado.visible = False
                exibir.update()
            else:
                encontrado.visible = False
                nao_encontrado.visible = True
        else:
            encontrado.visible = False
            nao_encontrado.visible = False
            exibir.content.controls = [ft.Text(value=f"{nome}: {almoxarifado[nome]} un.", size=15, color=ft.colors.BLACK) for nome in almoxarifado]

        encontrado.update()
        nao_encontrado.update()
        sleep(1)
        encontrado.visible = False
        nao_encontrado.visible = False
        encontrado.update()
        nao_encontrado.update()
        exibir.update()

    content = ft.Container(
        content=ft.Column(
            controls=[ 
                ft.Container(
                    content=ft.Column( 
                        controls=[
                            encontrado,
                            nao_encontrado,
                            ft.Text(
                                value="BUSCAS NO INVENTÁRIO",
                                size=15,
                                text_align=ft.TextAlign.RIGHT,
                                weight=ft.FontWeight.BOLD,
                                style=ft.TextStyle(color=ft.colors.BLACK,)
                            ),
                            ft.TextField(
                                content_padding=10,
                                icon=ft.icons.SEARCH,
                                value="ITEM",
                                text_style=ft.TextStyle(
                                    color=ft.colors.BLACK,
                                    weight=ft.FontWeight.BOLD,
                                ),
                                bgcolor=ft.colors.WHITE60,
                                capitalization=ft.TextCapitalization.CHARACTERS,
                                border_radius=ft.border_radius.all(0),
                                focused_bgcolor=ft.colors.PINK,
                                focused_color=ft.colors.WHITE,
                                focused_border_color=ft.colors.WHITE,
                                border=ft.InputBorder.UNDERLINE,
                                selection_color=ft.colors.BLACK,
                                input_filter=ft.InputFilter(
                                    allow=True,
                                    regex_string=r"[A-Za-zÁáÚúÉéÍíÂâÊêãÃ -]",
                                    replacement_string=""
                                ),
                                on_submit=buscar_almoxarifado
                            ),
                        ]
                    )
                ),
                ft.Row(
                    controls=[
                        exibir := ft.Container(
                            padding = ft.padding.all(10),
                            bgcolor=ft.colors.GREY_200,
                            height=350,
                            expand=True,
                            content=ft.Column(
                                scroll=ft.ScrollMode.AUTO,
                                wrap=True,
                                controls=[ft.Text(value=f"{nome}: {almoxarifado[nome]} un.", size=15, color=ft.colors.BLACK) for nome in almoxarifado]
                            )       
                        )
                    ]
                )
    
        ]
    ))
    return content


