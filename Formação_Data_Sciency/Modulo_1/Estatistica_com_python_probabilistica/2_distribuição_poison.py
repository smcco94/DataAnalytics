import numpy as np # type: ignore
from scipy.stats import poisson # type: ignore
import seaborn as sns # type: ignore
import pandas as pd # type: ignore
import matplotlib.pyplot as plt # type: ignore

#Poison
# É empregada para descrever o número de ocorrências em um intervalo de tempo ou espaço específico. 
# Os eventos são caracterizados pela possibilidade de contagem dos sucessos, mas a não possibilidade de contagem dos fracassos.
# Exemplo: Eu consigo contabilizar quantos buracos tem em um trecho na estrada, mas não consigo saber quantos "não" buracos existem

# Características
# 1. A probabilidade de uma ocorrência é a mesma em todo o intervalo observado.
# 2. O número de ocorrências em determinado intervalo é independente do número de ocorrências em outros intervalos.
# 3. A probabilidade de uma ocorrência é a mesma em intervalos de igual comprimento.

#Variaveis
# e = 2,17 .............
# u = representa o número médio de ocorrências em um determinado intervalo de tempo ou espaço
# k = número de sucessos no intervalo desejado

# Problema
# Um restaurante recebe em média 20 pedidos por hora. Qual a chance de que, em determinada hora escolhida ao acaso, o restaurante receba 15 pedidos?

#Média de ocorrencias por hora
media = 20
#Qual o numero de ocorrencias que queremos ober no periodo
k = 15

# Método 1
prob_met1 = ( (np.e ** (-media)) * (media ** k) ) / (np.math.factorial(k))

# Metodo 2
prob_met2 = poisson.pmf(k,media)

# QUIZ
# O número médio de clientes que entram em uma padaria por hora é igual a 20. 
# Obtenha a probabilidade de, na próxima hora, entrarem exatamente 25 clientes.

media_quiz = 20
k_quiz = 25
prob_cliente = poisson.pmf(k_quiz, media_quiz)

############# DESAFIO
media_des = 20
k_des = []
for i in range(40):
    k_des.append(i+1)
prob_des = (poisson.pmf(k_des,media_des)*100).round(1)

dados = pd.DataFrame({'QTD': k_des,'Chance':prob_des})
desv = dados.Chance.std()
#99,7% dados = 3 desvios padrões
lim_i = media_des - (desv*3)
lim_s = media_des + (desv*3)

dados_filter = dados.query("QTD >= {} and QTD <= {}".format(lim_i,lim_s))

### 100% dos dados
plt.figure(figsize=(12,4))
plot = sns.barplot(data = dados, x = 'QTD', y = 'Chance', color = 'gray', width = 0.9)
for i in plot.containers:
    plot.bar_label(i,)

### Com 3 desvios padrões a partir da média
plt.figure(figsize=(12,4))
plot = sns.barplot(data = dados_filter, x = 'QTD', y = 'Chance', color = 'gray', width = 0.9)
for i in plot.containers:
    plot.bar_label(i,)