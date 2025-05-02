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
