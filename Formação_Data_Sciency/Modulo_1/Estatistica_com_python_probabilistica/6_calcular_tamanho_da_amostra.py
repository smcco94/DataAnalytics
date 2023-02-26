import pandas as pd # type: ignore
import numpy as np # type: ignore
from scipy.stats import norm # type: ignore

dados = pd.read_csv('../files/dados.csv', sep=',')

##### Cáculo tamanho da amostra

# Obsevações
# 1. O desvio padrão ($\sigma$ ou $s$) e o erro ($e$) devem estar na mesma unidade de medida.
# 2. Quando o erro ($e$) for representado em termos percentuais, deve ser interpretado como um percentual relacionado à média.

# Z Tabelado
# 80% > z = 1,28
# 85% > z = 1,44
# 90% > z = 1,645
# 95% > z = 1,96
# 99% > z = 2,575

################################# Cálculo Para População INFINITA

# Variáveis

#### Com desvio padrão conhecido
    #n = (z*(sigma/e))**2
#### Com desvio padrão desconhecido
    #n = (z*(s/e))**2

# Onde:
# z = variável normal padronizada
# sigma = desvio padrão populacional
# s = desvio padrão amostral
# e = erro inferencial

##### Problema: 
# Estamos estudando o rendimento mensal dos chefes de domicílios no Brasil. 
# Nosso supervisor determinou que o erro máximo em relação a média seja de R$ 100,00. 
# Sabemos que o desvio padrão populacional deste grupo de trabalhadores é de R$ 3.323,39. 
# Para um nível de confiança de 95%, qual deve ser o tamanho da amostra de nosso estudo?

#para conjunto infinito é necessário uma amostra inicial para calculo dos demais itens

z = 1.96
sigma = 3323.39
e = 100

n = int(((z*(sigma/e))**2).__round__())

# Quiz 1

z_quiz = 1.645
sigma_quiz = 15
e_quiz = 4.55

n_quiz = int(((z_quiz*(sigma_quiz/e_quiz))**2).__round__())

################################# Cálculo Para População FINITA

# Variáveis

#### Com desvio padrão conhecido
    # n = ((z**2)*(sigma**2)*N) / ((z**2)*(sigma**2)+e**2(N-1))
#### Com desvio padrão desconhecido
    # n = ((z**2)*(s**2)*N) / ((z**2)*(s**2)+e**2(N-1))

# Onde:
# N = tamanho da população
# z = variável normal padronizada
# sigma = desvio padrão populacional
# s = desvio padrão amostral
# e = erro inferencial ou Margem de erro

##### Problema:
# Em um lote de 10.000 latas de refrigerante foi realizada uma amostra aleatória simples de 100 latas e 
# foi obtido o desvio padrão amostral do conteúdo das latas igual a 12 ml. 
# O fabricante estipula um erro máximo sobre a média populacional de apenas 5 ml. 
# Para garantir um nível de confiança de 95% qual o tamanho de amostra deve ser selecionado para este estudo?

N = 10000
z = 1.96
s = 12
e = 5

n = int((((z**2)*(s**2)*N) / ((z**2)*(s**2)+(e**2)*(N-1))).__round__())

# Quiz 2

s = 480
N = 2000
e = 300
z = 1.96

int((((z**2)*(s**2)*N) / ((z**2)*(s**2)+(e**2)*(N-1))).__round__())


################## DESAFIO FINITO

# O que levar em consideração ao calcular o tamanho da amostra
    # Se você quiser uma margem de erro menor, use um tamanho de amostra maior com a mesma população.
    # Quanto maior o nível de confiança de amostragem desejado, maior será o tamanho da amostra.
# É importante ter uma amostra com tamanho estatisticamente relevante?
    # Em geral, a regra é: 
    # quanto maior o tamanho da amostra, maior é a relevância estatística dela, ou seja, 
    # menor é a chance de os resultados serem apenas coincidência.



##### Margem de Erro

# Calculos para identificação de outliers
Q1 =  dados.Renda.quantile(.25)
Q3 =  dados.Renda.quantile(.75)
IIQ = Q3 - Q1
LI = Q1 - 1.5 * IIQ
LS = Q3 + 1.5 * IIQ

# Removendo Outliers
dados_new = dados[(dados.Renda >= LI) & (dados.Renda <= LS)]

# Amostra Aleatória
tamanho_amostra = 300
amostra_aleatoria = dados.Renda.sample(tamanho_amostra)

sigma = dados_new.Renda.std()
N = int(dados_new.Renda.shape[0])
z = 1.96
e_perc = ((z * (sigma/np.sqrt(tamanho_amostra))) / dados_new.Renda.mean()).__round__(3)
e_quant = (z * (sigma/np.sqrt(tamanho_amostra)))


##### Quantidade da Amostra

# Calculos para identificação de outliers
Q1 =  dados.Renda.quantile(.25)
Q3 =  dados.Renda.quantile(.75)
IIQ = Q3 - Q1
LI = Q1 - 1.5 * IIQ
LS = Q3 + 1.5 * IIQ

# Removendo Outliers
dados_new = dados[(dados.Renda >= LI) & (dados.Renda <= LS)]

Margem_erro_perc = 0.05
Margen_erro = Margem_erro_perc * dados_new.Renda.mean()
z_2 = 1.96
amostra_ideal = int(((pow(z_2,2))*(sigma**2)*N) / ((pow(z_2,2))*(sigma**2)+(Margen_erro**2)*(N-1)).round())



print('Sua amostra aleatória foi de {}, apresentando uma margem de erro de {}.\nNeste caso, sua amostra ideal para uma margem de erro de {} seria de {} com confiabilidade de 95%'.format(tamanho_amostra,e_perc,Margem_erro_perc,amostra_ideal))



################## DESAFIO INFINITO --> A população levada em consideração seria uma Amostra inicial