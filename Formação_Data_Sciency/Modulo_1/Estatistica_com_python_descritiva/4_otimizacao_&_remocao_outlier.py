import scipy as sp
import pandas as pd
import seaborn as sns
import numpy as np

dados = pd.read_csv('../files/dados.csv', sep=',')

# Calculos para identificação de outliers
Q1 =  dados.Renda.quantile(.25)
Q3 =  dados.Renda.quantile(.75)
IIQ = Q3 - Q1
LI = Q1 - 1.5 * IIQ
LS = Q3 + 1.5 * IIQ

dados_new = dados[(dados.Renda >= LI) & (dados.Renda <= LS)]

# Definindo o número de classes a partir da regra de Sturges
# K = 1 + (10/3)log10 n
# A regra de Sturges é um método para definição do número de classes, baseado no total de observações de uma variável;
n = dados_new.shape[0]
k = int((1 + (10 /3) * np.log10(n)).round(0))

# Criar tabela de frequência
freq = pd.value_counts(
    pd.cut(
        x = dados_new.Renda,
        bins = k, ## k encontrado pela regra de Sturges
        include_lowest = True
    ),
    sort = False # não classifica automático
)

perc = pd.value_counts(
    pd.cut(
        x = dados_new.Renda,
        bins = k,
        include_lowest = True
    ),
    sort = False, # não classifica automático
    normalize = True
).round(5) * 100

amp_fixa = pd.DataFrame(
    {'Frequência': freq, 'Porcentagem (%)': perc}
)

amp_fixa.rename_axis('Classes_Amplitude_Fixa', axis='columns', inplace=True)

# Gráfico de Barra
amp_fixa['Frequência'].plot.bar(width= 1, color= 'blue', alpha = 0.5, figsize= (10, 4))

# Gráfico Histograma
sns.histplot(dados_new.Renda,kde=True,kde_kws={'bw_adjust': 3,'cut': 3},bins=k) # type: ignore

### OBS
# bin = [200,800,1200,3000] --> Classifação
# 'cut' indica quantidade de desvio padrão a partir da mediana
    # 1 desvio padrão = 68% dos dados
    # 2 desvio padrão = 95% dos dados
    # 3 desvio padrão = 99,7% dos dados
# 'bw_adjust' Suaviza a curva