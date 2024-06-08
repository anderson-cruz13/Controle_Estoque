from data import *

data = '08/06/2024'
for data, infor in compras.items():
    print(data)
    for i in infor:
        hora = i['Hora']
        nome = i['Nome']
        quantidade = i['Quantidade']
        preco = i['R$']
