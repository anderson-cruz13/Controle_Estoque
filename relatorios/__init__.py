import flet as ft 
from data import vendas, compras


def interar_elementos_vendas():
    """Funções para pegar os elementos de vendas

    Returns:
        list: Lista de elementos existente em vendas
    """
    elementos = []
    for data, detalhes in vendas.items():
        for informacoes, lista in detalhes.items():
            id_pedido = informacoes # Número do pedio
            nome = lista[0] # Nome
            quantidade = lista[1] # Quantidade
            preco = lista[2] # Preço (não é preço por unidade, mas sim da venda)
            elementos.append(f"Data: {data} \n ID: {id_pedido} \n Nome: {nome} \n Quantidade: {quantidade} \n Preço: {preco}")
    return elementos

# Mesmo procedimento acima, no entando intera sobre um dict()
def interar_elementos_compras():
    """Função para pegar os elementos das compras

    Returns:
        list: lista elementos existente em compras
    """
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
    """Função que retorna o content para o frame

    Args:
        page (function): function vinda de main para redenrização
    """
    
    def interar_data(data, arquivo):
        """Função para buscar data em arquivo

        Args:
            data (str): text do TextField digitado pelo usuário
            arquivo (var composta): Poderá ser list ou dict | (vendas ou compras)

        Returns:
            list: elementos interados
        """
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
        """Função que recebe um evento

        Args:
            e (str): Recebe um evento de TextField
        """
        data = e.control.value
        relatorio = tittle.value

        data_arquivo = interar_data(data, relatorio)
        detalhes = [ft.Text(value=elemento, color=ft.colors.BLACK) for elemento in data_arquivo]
        contt.content.controls = detalhes
        contt.update()
          

    def change(e):
        """Função que muda o contt e tittle do conteudo de relatório

        Args:
            e (event): Recebe o value vindo do disprado on_click do TextButton em MenuBar
        """
        if e.control.text == 'Vendas':
            contt.content.controls = vendas_text_controls
            tittle.value = 'Vendas'
        else:
            contt.content.controls = compras_text_controls
            tittle.value = 'Compras'
        
        tittle.update()
        contt.update()

    vendas_elementos = interar_elementos_vendas() # Buscar elementos em vendas
    # Interar elementos em contt.controls
    vendas_text_controls = [ft.Text(value=elemento, color=ft.colors.BLACK) for elemento in vendas_elementos]
    compras_elementos = interar_elementos_compras() # Buscar elementos em compras
    # Interar elementos em contt.controls
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


