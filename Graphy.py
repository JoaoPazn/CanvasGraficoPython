# para baixar o matplotlib use #pip3 install matplotlib direto no terminal
# importa a biblioteca matplotlib
import matplotlib.pyplot as plt
# Importa o backend TkAgg do Matplotlib, ela é responsavel por exibir os gráficos utilizando a biblioteca Tkinter.
import matplotlib.backends.backend_tkagg as tkagg

# Criação do gráfico
# primeiro array = Y no gráfico, segundo array = X no gráfico
# obs, o primeiro e segundo array devem ter o a mesma quantidade de valores
plt.plot([1, 2, 3, 4, 5 , 6, 7, 8], [1, 4, 3, 5, 6, 10, 1, 3])

#Acessando a janela Tkinter
# pega a atual figura
fig = plt.gcf()
# chama o canvas
canvas = fig.canvas

# Alterando o título da janela usando o canvas
canvas.manager.window.title("canvas com 8 eixos")
# Mostra o gráfico
plt.show()

# para rodar o código dennovo feche a janela do gráfico atual.


#
# Gráfico Pizza
#


# # adiciona as categorias para o gráfico de pizza
# categorias = ['Maçã', 'Bananas', 'Cerejas', 'Laranjas', 'Queijo coalho'] 
# # adiciona a quantidade de cada valor, na mesma ordem que as categorias foram adicionadas
# valores = [30, 15, 45, 10, 200]

# # Cria o gráfico de pizza
# # Valores são adicionados para a porcentagem
# # labels=categorias cria o nome de cada valor.
# #autopct='%1.1f%%' mostra os valores em porcentagem em relação ao gráfico
# plt.pie(valores, labels=categorias, autopct='%1.1f%%')

# # Título opcional, aparece no topo do gráfico
# plt.title("Distribuição de Frutas")

# # Exibindo o gráfico
# fig = plt.gcf()
# # chama o canvas
# canvas = fig.canvas

# # Alterando o título da janela usando o canvas
# canvas.manager.window.title("canva pizza")
# # Mostra o gráfico
# plt.show()


#
# Gráfico de blocos
#


# # adiciona as categorias para o gráfico de pizza
# categorias = ['Gatos', 'Cachorros', 'Papagaios', 'Ratos domésticos']
# # adiciona a quantidade de cada valor.
# valores = [30, 70, 45, 300]

# # Cria o gráfico de blocos
# # categorias cria o nome de cada bloco
# # Valores são adicionados para a porcentagem
# # Color adiciona uma cor para os blocos, nome de cores podem ser encontrados em https://www.w3schools.com/colors/colors_names.asp, tambem pode ser usado o formato hexadeximal (#RRGGBB).
# plt.bar(categorias, valores, color='palegreen')

# # Adiciona o titulo
# plt.title('Petshop Análise Anual')
# # adiciona um texto em X
# plt.xlabel('Animais')
# # adiciona um texto em Y
# plt.ylabel('Quantidade de animais adotados esse Ano')


# # Exibindo o gráfico
# fig = plt.gcf()
# # chama o canvas
# canvas = fig.canvas

# # Alterando o título da janela usando o canvas
# canvas.manager.window.title("canva Colunas")
# # Mostra o gráfico
# plt.show()
