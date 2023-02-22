import scipy as sp
import pandas as pd
import seaborn as sns
import numpy as np

dados = pd.read_csv('../files/dados.csv', sep=',')

dados.Renda.min()
dados.Renda.max()

#Classificação
#A: acima de R$15.760,00;
#B: de R$7.880,00 até R$15.760,00;
#C: de R$3.152,00 até R$ 7.880,00;
#D: de R$1.576,00 até R$3.152,00;
#E: de zero até R$1.576,00.

classes = [0, 1576, 3152, 7880, 15760, dados.Renda.max()]
labels = ['E', 'D', 'C', 'B', 'A']

# Criando tabela de classes
classificacao = pd.cut(x = dados.Renda,
                    bins = classes,
                    labels = labels,
                    include_lowest = True)

# Vendo a frequencia das ocorreências aplicando o value_counts()
freq = pd.value_counts(classificacao)
perc = pd.value_counts(classificacao, normalize=True).round(4) * 100

dist_quant = pd.DataFrame({'Frequência': freq, "Porcentagem (%)": perc}).sort_index(ascending=True)
dist_quant.rename_axis('Classe',axis='columns',inplace=True)

# Hisitograma neste caso ficaria ruim por causa da distribuição, com isso podemos aproximar com graficos de barra
dist_quant['Frequência'].plot.bar(width= 1, color= 'blue', alpha = 0.5, figsize= (12, 6))
