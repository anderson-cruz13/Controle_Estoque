import flet as ft 
from data import *
from math import radians
from shop import *
from inventory import *
from sales import *
from relatorios import *

navigations_buttons = [
    {"nome": "Compras"},
    {"nome": "Inventário"},
    {"nome": "Vendas"},
    {"nome": "Relatórios"}
]

def main(page: ft.Page):
    page.window_always_on_top = True
    page.padding = ft.padding.all(0)
    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=ft.colors.PINK,
            primary_container=ft.colors.PINK_50,
            on_primary=ft.colors.PINK_100,
            on_primary_container=ft.colors.PINK_200,
        )
    )
    page.window_width = 550
    page.window_height = 700
    page.window_resizable = False
    page.window_full_screen = False
    page.window_title_bar_buttons_hidden = True

    def change(e):
        button = e.control.text
        if button == "Compras":
            frame.content = compras_content(page)
        elif button == "Inventário":
            frame.content = almoxarifado_content(page)
        elif button == "Vendas":
            frame.content = vendas_container(page)
        elif button == "Relatórios":
            frame.content = relatorios_container(page)
        frame.update()

    top = ft.Container(
        bgcolor=ft.colors.WHITE,
        height=100,
        content=ft.Row(
            controls=[
                ft.Container(
                    ft.Text(value="GESTÃO", weight=ft.FontWeight.BOLD, font_family="italic", 
                            color=ft.colors.PINK,),
                    col=4,
                ),
                ft.Container(
                    ft.Text(value="Olá, usuário!", size=16, weight=ft.FontWeight.BOLD, 
                            color=ft.colors.BLACK,),
                    col=4,
                ),
                ft.Container(
                    content=ft.Column(
                        controls=[
                                ft.Text(value="Data de hoje", size=16, weight=ft.FontWeight.BOLD, 
                                    color=ft.colors.BLACK,),
                                ft.Text(value=data, size=16, weight=ft.FontWeight.BOLD, 
                                    color=ft.colors.BLACK,),       
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_EVENLY
                    )

                )
            ], alignment=ft.MainAxisAlignment.SPACE_AROUND           
        )
    )

    main_button = [
        ft.FilledTonalButton(
            text=button["nome"],
            style=ft.ButtonStyle(
                color=ft.colors.WHITE,
                bgcolor=ft.colors.PINK_400, 
                shape=ft.RoundedRectangleBorder(radius=0)
            ),
            on_click=change
        ) for button in navigations_buttons
    ]

    navigation = ft.Container(
        content=ft.Row(
            controls=main_button,
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        bgcolor=ft.colors.WHITE60,
        padding=ft.padding.all(10),     
    )

    # Container Inicial
    frame = ft.Container(
    gradient=ft.LinearGradient(
        colors=[ft.colors.PINK_400, ft.colors.WHITE60],
        end=ft.Alignment(y=0, x=0.5),
        rotation=radians(-90)
    ),
    height=500,
    padding=ft.padding.all(10),
    content=ft.Row(
        controls=[
           ft.Text(
               value="Bem-Vind@!",
               size=25,
               color=ft.colors.WHITE,
               weight=ft.FontWeight.BOLD,
               text_align=ft.alignment.center
           )
        ],
        alignment=ft.MainAxisAlignment.CENTER
    ),
    expand=True,
)

    layout = ft.Column(
        spacing=0,
        controls=[
            top,
            navigation,
            frame,
        ],
        expand=True,
    )
    page.add(layout)
    
if __name__ == "__main__":
    ft.app(target=main)