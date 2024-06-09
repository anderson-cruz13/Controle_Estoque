# Descrição

Este projeto é uma aplicação de gestão de estoque desenvolvida utilizando o Flet, uma biblioteca Python que facilita a criação de interfaces gráficas de usuário (GUIs) modernas e interativas. A aplicação é dividida em quatro seções principais:

> Esse app possui uma interface gráfica, apesar de se ser responsive em demais plataformas, seu uso ainda está apenas em desktop.

---

## Compras: 
Permite registrar novas compras, incluindo fornecedor, data, produtos e quantidade.
## Inventário: 
Oferece uma visão geral do estoque atual, com detalhes sobre cada produto, como quantidade, valor unitário e valor total.
## Vendas: 
Permite registrar novas vendas, incluindo cliente, data, produtos e quantidade.
## Relatórios: 
Gera relatórios de compras, vendas e estoque, permitindo análise e tomada de decisões estratégicas.

---

# Funcionalidades

- [x] Interface gráfica intuitiva e amigável.
- [x] Navegação fácil entre as seções.
- [x] Registro de compras e vendas com detalhes.
- [x] Visão geral do estoque atual.
- [x] Geração de relatórios personalizados.
- [x] Salvamento e carregamento de dados para persistência entre sessões.
- [ ] Tela de login.
- [ ] Opção de editar vendas.
- [ ] Cadastrar (funcionários / clientes).
      
# Tecnologias Utilizadas

1. Python
2. Flet
3. Pickle

# Interface do Usuário

A interface do usuário é organizada em uma janela fixa com 550 pixels de largura e 700 pixels de altura, que *não pode ser redimensionada*. A aplicação inclui:

***
Cabeçalho com saudação ao usuário, data atual e nome "GESTÃO" em destaque.
Botões tonalizados preenchidos para navegação entre as seções.
Área principal que exibe o conteúdo da seção selecionada.
Gradientes de cores para um toque visual atraente.
Informações de desenvolvimento e contato (visíveis apenas em janelas com largura suficiente).
***

# Considerações Adicionais

O código garante que a interface se adapte a diferentes tamanhos de tela.
Os dados são salvos e carregados de forma segura e eficiente.
A aplicação pode ser facilmente extendida para incluir novas funcionalidades.

# Conclusão

Esta aplicação de gestão de estoque oferece uma solução completa e integrada para gerenciar suas operações de forma eficiente. A interface intuitiva, a variedade de funcionalidades e a facilidade de uso a tornam uma ferramenta valiosa para empresas de todos os portes.

# Observações:

É preciso trabalhar ainda na interface de login, tornar mais dinâmico e colocar mais funcionalidades.
