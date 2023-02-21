import scipy as sp
import pandas as pd
import seaborn as sns
import numpy as np

dados = pd.read_csv('../files/dados.csv', sep=',')

# Quartis
dados.Renda.quantile([0.25, 0.5, 0.75])

# Decis
dados.Idade.quantile([i / 10 for i in range(1, 10)])

# Percentil
dados.Renda.quantile([i / 100 for i in range(1, 100)])

# Cumulativo c/ decis para auxiliar na visualização
ax = sns.distplot(dados.Idade,
                  hist_kws = {'cumulative': True},
                  kde_kws = {'cumulative': True},
                  bins = 10)
ax.figure.set_size_inches(14, 6)
ax.set_title('Distribuição de Frequências Acumulada', fontsize=18)
ax.set_ylabel('Acumulado', fontsize=14)
ax.set_xlabel('Anos', fontsize=14)
dados.Idade.quantile([i / 10 for i in range(1, 10)])

# Boxplot
# criando boxplot e ajustando orientação
ax = sns.boxplot( x = 'Altura', data = dados, orient = 'h')
ax.figure.set_size_inches(12, 4)
ax.set_title('Altura', fontsize=18)
ax.set_xlabel('Metros', fontsize=14)
# criando boxplot com comparação inserindo o eixo y
ax = sns.boxplot( x = 'Altura', y = 'Sexo', data = dados, orient = 'h')
ax.figure.set_size_inches(12, 4)
ax.set_title('Altura', fontsize=18)
ax.set_xlabel('Metros', fontsize=14)
# criando boxplot com auxilio de query
ax = sns.boxplot( x = 'Renda', data = dados.query('Renda < 10000'), orient = 'h')
ax.figure.set_size_inches(12, 4)
ax.set_title('Renda', fontsize=18)
ax.set_xlabel('R$', fontsize=14)