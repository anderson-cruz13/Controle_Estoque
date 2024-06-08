import flet as ft 

alfa_TextField = ft.TextField(
    content_padding=20,
    width=200,
    value="",
    label="Nome",
    label_style=ft.TextStyle(
        color=ft.colors.BLACK,
        weight=ft.FontWeight.BOLD,
    ),
    text_style=ft.TextStyle(
    weight=ft.FontWeight.BOLD,
    color=ft.colors.BLACK
    ),
    bgcolor=ft.colors.WHITE,
    border=ft.InputBorder.OUTLINE,
    border_color=ft.colors.BLACK,
    capitalization=ft.TextCapitalization.CHARACTERS,
    border_radius=ft.border_radius.all(0),
    focused_bgcolor=ft.colors.PINK,
    focused_color=ft.colors.WHITE,
    focused_border_color=ft.colors.PINK_100,
    input_filter= ft.InputFilter(
                allow=True,
                regex_string=r"[A-Za-zÁáÚúÉéÍíÂâÊêãÃ -]",
                replacement_string=""
    ),   
    selection_color=ft.colors.BLACK           
)

int_TextField = ft.TextField(
    value=0,
    content_padding=20,
    width=500,
    label="Quantidade",
    label_style=ft.TextStyle(
        color=ft.colors.BLACK,
        weight=ft.FontWeight.BOLD,
    ),
    text_style=ft.TextStyle(
    weight=ft.FontWeight.BOLD,
    color=ft.colors.BLACK
    ),
    bgcolor=ft.colors.WHITE,
    border=ft.InputBorder.OUTLINE,
    border_color=ft.colors.BLACK,
    border_radius=ft.border_radius.all(0),
    focused_bgcolor=ft.colors.PINK,
    focused_color=ft.colors.WHITE,
    focused_border_color=ft.colors.PINK_100,
    input_filter= ft.InputFilter(
                allow=True,
                regex_string=r"[0-9]",
                replacement_string=""
    ),   
    selection_color=ft.colors.BLACK          
)

float_TextField = ft.TextField(
    value=0,
    content_padding=20,
    width=500,
    label="Preço",
    label_style=ft.TextStyle(
        color=ft.colors.BLACK,
        weight=ft.FontWeight.BOLD,
    ),
    text_style=ft.TextStyle(
    weight=ft.FontWeight.BOLD,
    color=ft.colors.BLACK
    ),
    bgcolor=ft.colors.WHITE,
    border=ft.InputBorder.OUTLINE,
    border_color=ft.colors.BLACK,
    border_radius=ft.border_radius.all(0),
    focused_bgcolor=ft.colors.PINK,
    focused_color=ft.colors.WHITE,
    focused_border_color=ft.colors.PINK_100,
    input_filter= ft.InputFilter(
                allow=True,
                regex_string=r"[0-9,.]",
                replacement_string=""
    ),   
    prefix_text="R$",
    prefix_style=ft.TextStyle(
        size=16,
        color=ft.colors.BLACK,
        weight=ft.FontWeight.BOLD
    ),
    selection_color=ft.colors.BLACK, 
)

txt_salvos = ft.FilledButton(text="SUCESSO", width=300, height=30, visible=False, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0), bgcolor=ft.colors.GREEN, color=ft.colors.WHITE))
txt_erros = ft.FilledButton(text="ERROR", width=300, height=30, visible=False, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0), bgcolor=ft.colors.RED, color=ft.colors.WHITE))

# Função para verificar se o input tem virgula e fazer substituição por ponto
def verificar(preco):
    """Verificação de float

    Args:
        preco (_type_): _description_

    Returns:
        _type_: _description_
    """
    try:
        preco = preco.replace(',', '.')
        return float(preco)
    except ValueError:
        return 0
