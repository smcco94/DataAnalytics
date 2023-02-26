import pandas as pd # type: ignore
import numpy as np # type: ignore
from scipy.stats import norm # type: ignore

dados = pd.read_csv('../files/dados.csv', sep=',')

########## Teorema do Limite Central

# Teorema do Limite Central afirma que, com o aumento do tamanho da amostra, a distribuição das médias 
# amostrais se aproxima de uma distribuição normal com média igual à média da população e desvio padrão igual 
# ao desvio padrão da variável original dividido pela raiz quadrada do tamanho da amostra. 
# Este fato é assegurado para n maior ou igual a 30.

tamanho_amostra = 1000
total_de_amostras = 200
amostras = pd.DataFrame()
for i in range(total_de_amostras):
  _ = dados.Idade.sample(tamanho_amostra)
  _.index = range(0, len(_)) # type: ignore
  amostras['Amostra{}'.format(i)] = _ 

amostras.mean().hist()

# Comparando médias
dados.Idade.mean()
amostras.mean().mean()

# Comparando Desvio Padrão
amostras.mean().std()
dados.Idade.std() / np.sqrt(tamanho_amostra) # type: ignore

########## Intervalo de Confiança

# Suponha que os pesos dos sacos de arroz de uma indústria alimentícia se distribuem aproximadamente como uma normal 
# de desvio padrão populacional igual a 150 g. Selecionada uma amostra aleatório de 20 sacos de um lote 
# específico, obteve-se um peso médio de 5.050 g. Construa um intervalo de confiança para a 
# média populacional assumindo um nível de significância de 5%.

media_amostra = 5050
significancia = 0.05
confianca = 1 - significancia

# Z Tabelado
# 90% > z = 1,645
# 95% > z = 1,96
# 99% > z = 2,575

# Z Calculado
# Variavel = 95% confiabilidade --> (100 - (( 100 - 95 ) / 2)) / 100
# Z = norm.ppf(variavel)

z = norm.ppf(0.975) # Variável
desv_pop = 150
n = 20
raiz_n = np.sqrt(n)
sigma = desv_pop / raiz_n
e = z * sigma

intervalo = norm.interval(alpha = 0.95, loc = media_amostra, scale = sigma)

# Quiz 1
quiz_n = 50
quiz_desv = 6
z = 1.96
sigma = quiz_desv / np.sqrt(quiz_n)
e = z * sigma
print(e)

# Quiz 2
quiz_n2 = 1976
quiz_desv2 = 11
quiz_media = 28
z = 1.645
quiz_sigma = quiz_desv2 / np.sqrt(quiz_n2)
quiz_intervalo = norm.interval(alpha = 0.9, loc = quiz_media, scale = quiz_sigma)
e = z * quiz_sigma
print(quiz_intervalo)
