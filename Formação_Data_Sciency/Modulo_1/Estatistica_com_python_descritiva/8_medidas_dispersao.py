import scipy as sp # type: ignore
import pandas as pd # type: ignore
import seaborn as sns # type: ignore
import numpy as np # type: ignore

dados = pd.read_csv('../files/dados.csv',sep=',')

################### Desvio médio absoluto
#Vai sair do python
dados.Renda.mad()
#Novo método
(dados.Renda - dados.Renda.mean()).abs().mean()

df = pd.DataFrame(data = {'Fulano': [8, 10, 4, 8, 6, 10, 8],
                          'Sicrano': [7.5, 8, 7, 8, 8, 8.5, 7]}, 
                  index = ['Matemática', 
                           'Português', 
                           'Inglês', 
                           'Geografia', 
                           'História', 
                           'Física', 
                           'Química'])
df.rename_axis('Matérias', axis = 'columns', inplace = True)
# Calulando o desvio, sendo ele a diferença da nota em relação a média das notas
notas_fulano = df[['Fulano']]
nota_media_fulano = notas_fulano.mean()[0] # type: ignore
notas_fulano['|Desvio|'] = (notas_fulano['Fulano'] - nota_media_fulano).abs()
notas_fulano['(Desvio)^2'] = notas_fulano['|Desvio|'].pow(2)
# Calculando o desvio médio absoluto
#Vai sair do python
df['Fulano'].mad()
#Novo método
(df['Sicrano'] - df['Sicrano'].mean()).abs().mean()


################### Variância
# Sem função
notas_fulano['(Desvio)^2'].sum()/(notas_fulano.shape[0] -1) # type: ignore
# Com função
variancia = notas_fulano['Fulano'].var()

################### Desvio padrão
# Sem função
np.sqrt(variancia) # type: ignore
# Com função
desvio_padrao = notas_fulano['Fulano'].std()


