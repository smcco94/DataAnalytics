import pandas as pd

#importando arquivos
dados = pd.read_csv('files/aluguel_residencial.csv', sep=';')

#verificando dados
dados.notnull() # verifica não nulo, retorna nao nulo como true
dados.isnull() # verifica nulo, retorna nulo como true
dados.info()

#Verificando valores nulos da coluna valor
dados[dados.Valor.isnull()]

#Limpando dados nulos da coluna valor
dados.dropna(subset='Valor', inplace=True)

#Limpando tipo apartamento que não possui valor
dados[dados.Valor.isnull()]

#Verificando dados nulos para condominio
dados[dados['Condominio'].isnull()].shape[0]

#Selecionando apartamentos com condominios nulos
selecao = (dados['Tipo'] == 'Apartamento') & (dados['Condominio'].isnull())

#Retirandos apartamentos com condominios nulos do dataframe
dados = dados[~selecao]

#Substituindo valores nulos para 0 de determinadas colunas
dados = dados.fillna({'Condominio': 0, 'IPTU': 0})

#exportando tabela tratada
dados.to_csv('files/aluguel_residencial_tratado.csv', sep=';')

################# EXTRA ##################

data = [0.5, None, None, 0.52, 0.54, None, None, 0.59, 0.6, None, 0.7]
s = pd.Series(data)

#Interpola os dados de baixo pra cima com o ultimo valor válido
s.fillna(method = 'ffill', limit = 1) # limit = 1 -> indica fazer isso no maximo 1x 

#Interpola os dados de cima pra baixo com o ultimo valor válido
s.fillna(method = 'bfill')

#Método pandas
s.interpolate(method='linear')

### Métodos

# 'linear': Ignore o índice e trate os valores como igualmente espaçados. Este é o único método suportado em MultiIndexes.
#'time': Funciona em dados diários e de alta resolução para interpolar determinado comprimento de intervalo.
#'índice', 'valores': use os valores numéricos reais do índice.
#'pad': Preencha NaNs usando valores existentes.
#'mais próximo', 'zero', 'linear', 'quadrático', 'cúbico', 'spline', 'baricêntrico', 'polinomial': Passado para scipy.interpolate.interp1d . Esses métodos usam os valores numéricos do índice. Ambos 'polynomial' e 'spline' requerem que você também especifique uma ordem (int), por exemplo .df.interpolate(method='polynomial', order=5)
#'krogh', 'piecewise_polynomial', 'spline', 'pchip', 'akima', 'cubicspline': Wrappers em torno dos métodos de interpolação SciPy de nomes semelhantes. Consulte Notas .
#'from_derivatives': Refere-se a scipy.interpolate.BPoly.from_derivatives que substitui o método de interpolação 'piecewise_polynomial' em scipy 0.18.