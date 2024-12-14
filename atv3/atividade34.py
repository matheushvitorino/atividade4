import pandas as pd

# Criar um DataFrame
dados = {
    'Aluno': ['João', 'Maria', 'Pedro', 'Ana'],
    'Nota': [8.5, 9.0, 7.5, 8.0],
    'Faltas': [2, 0, 5, 1]
}
df = pd.DataFrame(dados)

print("DataFrame:\n", df)
print("\nCabeçalho do DataFrame:")
print(df.head())

print("\nInformações do DataFrame:")
print(df.info())

print("\nEstatísticas Descritivas:")
print(df.describe())


filtro = df[df['Nota'] > 8]
print("\nAlunos com nota maior que 8:")
print(filtro)
