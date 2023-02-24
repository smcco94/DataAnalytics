import scipy as sp
import pandas as pd
import seaborn as sns
import numpy as np

dados = pd.read_csv('../files/dados.csv', sep=',')

ax = sns.distplot(dados.Altura, kde = True) # kde indica linha de densidade
ax.figure.set_size_inches(12, 6)
ax.set_title('Distribuição de Frequências - Altura', fontsize=18)
ax.set_xlabel('Metros', fontsize=14)
media = dados.Altura.mean().__round__(4)
ax.axvline(dados.Altura.mean(), color='r', linestyle='solid', linewidth=1, label='Média: %s' %(media))
ax.legend()
ax