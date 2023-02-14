import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Lê arquivo csv
df = pd.read_csv("../files/ratings.csv")

# printa primeiras 10 linhas
df.head(10)

#Renomeia coluna
df.columns = ["UsuarioID","FilmeID","Nota","Momento"]

#verifica tipo
type(df)

#printa coluna
df.Nota
df['Nota']

#contagem de valores
df['Nota'].value_counts()
df.Nota.value_counts()

#média das notas
df['Nota'].mean()
df.Nota.mean()

#Gráfico info adicional (https://matplotlib.org/stable/plot_types/index.html)
df.Nota.plot(kind='hist')
plt.axvline(df.Nota.median(), color='k', linestyle='dashed', linewidth=1, label='sine')
plt.axhline(df.Nota.value_counts().mean(), color='k', linestyle='dashed', linewidth=1)

#boxplot
df.Nota.plot(kind='box', vert=False)

#mediana e media
print("Média",df.Nota.mean())
print("Mediana",df.Nota.median())

#Conjunto de informações
df.Nota.describe()

#Boxplot
sns.boxplot(df.Nota)