import numpy as np

# Criando uma matriz 3x3
matriz = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print("Matriz:\n", matriz)
# Média, desvio padrão e soma ao longo de um eixo
media = np.mean(matriz, axis=0)  # Média por coluna
desvio_padrao = np.std(matriz, axis=0)  # Desvio padrão por coluna
soma = np.sum(matriz, axis=0)  # Soma por coluna

print("Média (por coluna):", media)
print("Desvio Padrão (por coluna):", desvio_padrao)
print("Soma (por coluna):", soma)
