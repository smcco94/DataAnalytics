import pandas as pd # type: ignore
import numpy as np # type: ignore
from scipy.stats import norm # type: ignore

dados = pd.read_csv('../files/dados.csv', sep=',')

# Distribuição normaç
# A distribuição normal é uma das mais utilizadas em estatística. É uma distribuição contínua, onde a 
# distribuição de frequências de uma variável quantitativa apresenta a forma de sino e é simétrica em relação a sua média.

# Características
# 1. É simétrica em torno da média;
# 2. A área sob a curva corresponde à proporção 1 ou 100%;
# 3. As medidas de tendência central (média, mediana e moda) apresentam o mesmo valor;
# 4. Os extremos da curva tendem ao infinito em ambas as direções e, teoricamente, jamais tocam o eixo $x$;
# 5. O desvio padrão define o achatamento e largura da distribuição. Curvas mais largas e mais achatadas apresentam valores maiores de desvio padrão;
# 6. A distribuição é definida por sua média e desvio padrão;
# 7. A probabilidade sempre será igual à área sob a curva, delimitada pelos limites inferior e superior.

### Tabela normal
tabela_normal_padronizada = pd.DataFrame(
    [], 
    index=["{0:0.2f}".format(i / 100) for i in range(0, 400, 10)],
    columns = ["{0:0.2f}".format(i / 100) for i in range(0, 10)])

for index in tabela_normal_padronizada.index:
    for column in tabela_normal_padronizada.columns:
        Z = np.round(float(index) + float(column), 2)
        tabela_normal_padronizada.loc[index, column] = "{0:0.4f}".format(norm.cdf(Z))
tabela_normal_padronizada.rename_axis('Z', axis = 'columns', inplace = True)

# Problema
# Em um estudo sobre as alturas dos moradores de uma cidade verificou-se que o conjunto de dados segue uma 
# distribuição aproximadamente normal,com média 1,70 e desvio padrão de 0,1. 
# Com estas informações obtenha o seguinte conjunto de probabilidades:
# 1 probabilidade de uma pessoa, selecionada ao acaso, ter menos de 1,80 metros.
media = 1.7
desv_pad = 0.1
Z = (1.8 - media) / desv_pad
# procurando na tabela tenho que
prob_tabela = 0.8413
# utilizando função norm 
prob_norm = norm.cdf(Z)

# Quiz 1
media_q1 = 70
desv_pad_q1 = 5
prob_q1 = norm.cdf((85 - media_q1) / desv_pad_q1) # Z = (Valor de Consulta - Média) / desvio padrão

# 2 probabilidade de uma pessoa, selecionada ao acaso, ter entre 1,60 metros e 1,80 metros.   

Z_inferior = (1.6 - media) / desv_pad
Z_superior = (1.8 - media) / desv_pad
# Método 1
norm.cdf(Z_superior) - (1 - norm.cdf(Z_superior)) # type: ignore
# Método 2
norm.cdf(Z_superior) - norm.cdf(Z_inferior) # type: ignore

# Quiz 2

media_q2 = 300
desv_pad_q2 = 50
norm.cdf((350 - media_q2) / desv_pad_q2) - norm.cdf((250 - media_q2) / desv_pad_q2) # type: ignore
norm.cdf((500 - media_q2) / desv_pad_q2) - norm.cdf((400 - media_q2) / desv_pad_q2) # type: ignore

# 3 probabilidade de uma pessoa, selecionada ao acaso, ter mais de 1,90 metros.
# Pega o limite superior, calcula toda a area abaixo e faz o total menos ela
# Metodo 1
prob_3_1 = 1 - norm.cdf((1.9 - media) / desv_pad)
# Metodo 2
prob_3_2 = norm.cdf(-((1.9 - media) / desv_pad))

# Quiz 3
media_q3 = 720
desv_pad_q3 = 30
# 1) Entre 650 e 750 dias
prob_q3_1 = norm.cdf((750 - media_q3) / desv_pad_q3) - norm.cdf((650 - media_q3) / desv_pad_q3)
# 2) Mais que 800 dias
prob_q3_2 = norm.cdf(-((800 - media_q3) / desv_pad_q3))
# 3) Menos que 700 dias
prob_q3_3 = norm.cdf((700 - media_q3) / desv_pad_q3)
# Resposta
print('{},{},{}'.format(prob_q3_1*100,prob_q3_2*100,prob_q3_3*100))

# Quiz 4
# 1) Z < 1,96
z1 = norm.cdf(1.96)
# 2) Z > 2,15
z2 = norm.cdf(-2.15)
# 3) Z < -0,78
z3 = norm.cdf(-0.78)
# 4) Z > 0,59
z4 = norm.cdf(-0.59)
# Resposta
print('{},{},{},{}'.format(z1,z2,z3,z4))