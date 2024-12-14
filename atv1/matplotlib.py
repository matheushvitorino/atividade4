import matplotlib.pyplot as plt

# Dados de exemplo
dias = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom']
temperaturas = [22, 24, 19, 23, 25, 20, 18]

# Criar o gráfico de linha
plt.plot(dias, temperaturas, marker='o', linestyle='-', color='b')
plt.title('Variação de Temperatura (°C)')
plt.xlabel('Dias da Semana')
plt.ylabel('Temperatura (°C)')
plt.grid(True)
plt.show()
