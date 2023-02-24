import scipy as sp #sp.__version__
import pandas as pd #pd.__version__
import seaborn as sns #sns.__version__
import numpy as np #np.__version__

#exemplo de versionamento de bibliotecas --> !pip install pandas=='0.2.1'

dados = pd.read_csv('../files/dados.csv', sep=',')

######## quantitativos = mensuráveis, qualitativos = atributos || qualidade ################
#qualitativa ordinal - variáveis podem ser ordenadas ou hierarquizadas
dados['Anos de Estudo'].unique()
#qualitativa nominais - variáveis não podem ser ordenadas ou hierarquizadas
dados['UF'].unique()
dados['Sexo'].unique()
dados['Cor'].unique()
#quantitavia discretos - variaveis que representam um contagem onde os valores possíveis formam um conjunto finito ou enumerável
dados['Idade'].min()
dados['Idade'].max()
print('De %s até %s anos' % (dados.Idade.min(), dados.Idade.max()))
#quantitativa contínuos - representa o valor exato, sendo representado por fração, mas uma idade pode também ser dividida
# por faixas, assim viraria uma qualitativa ordinal
print('De %s até %s anos' % (dados.Altura.min(), dados.Altura.max()))
