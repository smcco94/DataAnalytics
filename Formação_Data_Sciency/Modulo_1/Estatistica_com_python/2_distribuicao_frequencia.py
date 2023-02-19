import scipy as sp
import pandas as pd
import seaborn as sns
import numpy as np

dados = pd.read_csv('../files/dados.csv', sep=',')

#Qualitativas
#Método 1
freq = dados.Sexo.value_counts()
perc = dados.Sexo.value_counts(normalize=True)*100 # normalize mostra percentualmente
dist_qualitativa = pd.DataFrame({'Frequência': freq, "Porcentagem (%)": perc})
dist_qualitativa.rename(index = {0: 'Masculino', 1: 'Feminino'}, inplace = True)
dist_qualitativa.rename_axis('Sexo', axis = 'columns', inplace = True)

#Método 2
sexo = {0: 'Masculino',
        1: 'Feminino'}
cor = {0: 'Indígena',
        2: 'Branca',
        4: 'Preta',
        6: 'Amarela',
        8: 'Parda',
        9: 'Sem declaração'}

frequencia = pd.crosstab(dados.Sexo,
                         dados.Cor) 
frequencia.rename(index = sexo, inplace = True)
frequencia.rename(columns = cor, inplace = True)
frequencia

percentual = pd.crosstab(dados.Sexo,
                         dados.Cor,
                         normalize = True).round(3) * 100
percentual.rename(index = sexo, inplace = True)
percentual.rename(columns = cor, inplace = True)
percentual

#Método 2 com função de agregação
percentual = pd.crosstab(dados.Sexo,
                         dados.Cor,
                         aggfunc = 'mean',
                         values = dados.Renda).round(2)
percentual.rename(index = sexo, inplace = True)
percentual.rename(columns = cor, inplace = True)
percentual