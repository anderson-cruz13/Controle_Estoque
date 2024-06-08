import flet as ft 
from data import vendas, compras


def interar_elementos_vendas():
    elementos = []
    for data, detalhes in vendas.items():
        for informacoes, lista in detalhes.items():
            id_pedido = informacoes
            nome = lista[0]
            quantidade = lista[1]
            preco = lista[2]
            elementos.append(f"Data: {data} \n ID: {id_pedido} \n Nome: {nome} \n Quantidade: {quantidade} \n Preço: {preco}")
    return elementos

def interar_elementos_compras():
    elementos = []
    for data, infor in compras.items():
        for i in infor:
            hora = i['Hora']
            nome = i['Nome']
            quantidade = i['Quantidade']
            preco = i['R$']
            elementos.append(f"Data: {data} \n Hora: {hora} \n Nome: {nome}\n Quantidade: {quantidade}\n Preço: {preco}")
    return elementos

def relatorios_container(page):
    
    def interar_data(data, arquivo):
        elementos = []
        if arquivo == "Vendas":
            detalhes = vendas.get(data, {})
            for id_pedido, lista in detalhes.items():
                nome = lista[0]
                quantidade = lista[1]
                preco = lista[2]
                elementos.append(f"Data: {data} \n ID: {id_pedido} \n Nome: {nome} \n Quantidade: {quantidade} \n Preço: {preco}")
        elif arquivo == "Compras":
            detalhes = compras.get(data, [])
            for i in detalhes:
                hora = i['Hora']
                nome = i['Nome']
                quantidade = i['Quantidade']
                preco = i['R$']
                elementos.append(f"Data: {data} \n Hora: {hora} \n Nome: {nome}\n Quantidade: {quantidade}\n Preço: {preco}")
        return elementos

    def buscar(e):
        data = e.control.value
        relatorio = tittle.value

        data_arquivo = interar_data(data, relatorio)
        detalhes = [ft.Text(value=elemento, color=ft.colors.BLACK) for elemento in data_arquivo]
        contt.content.controls = detalhes
        contt.update()
          

    def change(e):
        if e.control.text == 'Vendas':
            contt.content.controls = vendas_text_controls
            tittle.value = 'Vendas'
        else:
            contt.content.controls = compras_text_controls
            tittle.value = 'Compras'
        
        tittle.update()
        contt.update()

    vendas_elementos = interar_elementos_vendas()
    vendas_text_controls = [ft.Text(value=elemento, color=ft.colors.BLACK) for elemento in vendas_elementos]
    compras_elementos = interar_elementos_compras()
    compras_text_controls = [ft.Text(value=elemento, color=ft.colors.BLACK) for elemento in compras_elementos]

    content = ft.ResponsiveRow(
        controls=[
            ft.MenuBar(
                style=ft.MenuStyle(bgcolor=ft.colors.PINK,),
                controls=[
                    ft.SubmenuButton(
                        content=ft.Text("Vendas"),
                        controls=[ft.TextButton(text="Vendas", icon=ft.icons.PREVIEW, 
                                                on_click=change),],),
                    ft.SubmenuButton(
                        content=ft.Text("Compras"),
                        controls=[ft.TextButton(text="Compras", icon=ft.icons.PREVIEW,
                                                on_click=change)]),
                ],
            ),
            ft.Container(
                content= ft. Column([
                    tittle := ft.Text(value="", weight=ft.FontWeight.BOLD, color=ft.colors.BLACK,),
                    ft.TextField(value="Data", 
                         bgcolor=ft.colors.WHITE,
                         color=ft.colors.BLACK,
                         focused_bgcolor=ft.colors.PINK,
                         focused_border_color=ft.colors.WHITE,
                         focused_color=ft.colors.WHITE,
                         border_radius=ft.border_radius.all(0),
                         border=ft.InputBorder.OUTLINE,
                         input_filter=ft.InputFilter(
                             allow=True,
                             regex_string=r"[0-9/TODOtodo]"
                         ),
                         selection_color=ft.colors.PINK_300,
                         on_submit=buscar),
                    
                    ft.Row(
                        controls=[
                            contt:= ft.Container(
                                padding=ft.padding.all(10),
                                bgcolor=ft.colors.WHITE60,
                                height=500,
                                expand=True,
                                content=ft.Column(
                                    spacing=5,
                                    scroll=ft.ScrollMode.AUTO,
                                    wrap=True,
                                    controls=''))],
                                    )])),
        ],
    )
    
    return content


