# Importando o pandas e o matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Importando a base em csv
df = pd.read_csv('file.csv')

# Analisando as 5 primeiras linhas, as 5 últimas e um resumo do total:
df.head()
df.tail()
display(df)

# Mostrando somente o tipo dos dados
df.dtypes

# Mostrando o tipo de dados e os valores vazios
df.info()

# Contando os valores vazios por coluna
df.isnull().sum()

# montando uma base via diccionário:
base = {
    'Y': [1,2,3,4,5,6,7,8,9,10,11]
}

df2 = pd.DataFrame(base)

# Mostrando a média
df2.mean()

# Mostrando a contagem de registros
df2.count()

# Mediana
df2.median()

# Desvio Padrão
df2.std()

# Trazendo todo o resumo estatístico utilizando o describe da primeira base
df.describe()

# Usando colunas
df['Column']

# Usando uma coluna, podemos contar a quantidade de vezes que cada valor aparece
df.Column2.value_counts()

# Selecionando um conjunto de colunas
df[['Column1','Column2','Column3']]

# Verificando os dados da primeira coluna que são maiores que 100 
df[df.Column1 > 100]

# utilizando .loc() para verificar os 5 primeiros maiores que 100
df.loc[(df.Column1 > 100).head()

# historigrama simples utilizando matplotlib:
df.column1.hist(bins=100);

# utilizando barra
df.column2.plot.bar();
