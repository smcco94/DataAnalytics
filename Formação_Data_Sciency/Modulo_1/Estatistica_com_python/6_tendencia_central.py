import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dados = pd.read_csv('../files/dados.csv', sep=',')

# Média, útil porém sensivel aos extremos, cuidado, deve-se conhecer bem o dataset
#agrupado por sexo
dados.groupby(dados.Sexo).Renda.mean()

# Mediana
dados.groupby(dados.Sexo).Renda.median()

# Moda muito utilizada em valors qualitativos, mostra valores que mais se repetem
df.mode() # type: ignore
dados.Altura.mode()

# Assimetrico a esquerda
ax = sns.distplot(dados.query('Renda < 20000').Renda, kde_kws={'bw_adjust':3, 'cut':3})
ax.axvline(dados.Renda.mode().max(), color='r', linestyle='solid', linewidth=1, label= "Moda")
ax.axvline(dados.Renda.median(), color='g', linestyle='solid', linewidth=1)
ax.axvline(dados.Renda.mean(), color='b', linestyle='solid', linewidth=1)
ax.legend(labels = ["Média", "Moda", "Mediana"])
ax.figure.set_size_inches(12, 6)

# Assimetrico a direita
ax = sns.distplot(dados['Anos de Estudo'], bins = 17, kde_kws={'bw_adjust':6, 'cut':3})
ax.axvline(dados['Anos de Estudo'].mode().max(), color='r', linestyle='solid', linewidth=1, label= "Moda")
ax.axvline(dados['Anos de Estudo'].median(), color='g', linestyle='solid', linewidth=1)
ax.axvline(dados['Anos de Estudo'].mean(), color='b', linestyle='solid', linewidth=1)
ax.figure.set_size_inches(12, 6)

# Simetrico
ax = sns.distplot(dados.Altura)
ax.axvline(dados.Altura.mode().mean(), color='r', linestyle='solid', linewidth=1)
ax.axvline(dados.Altura.median(), color='g', linestyle='solid', linewidth=1)
ax.axvline(dados.Altura.mean(), color='b', linestyle='solid', linewidth=1)
ax.legend(labels = ["Média", "Moda", "Mediana"])
ax.figure.set_size_inches(12, 6)

