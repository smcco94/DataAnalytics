import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv('files/aluguel_residencial_tratado_agregado.csv', sep=';')

#Gráfico antes
print('Gráfico antes de remover outliers\n')
plt.rc('figure', figsize = (12,4))
plt.boxplot(dados.Valor, vert=True)
plt.title("Valor de Locação de Imóveis", loc="center", fontsize=18)
plt.ylabel("Valor de Locação")
plt.show()

# Calculos para identificação de outliers
Q1 = dados.Valor.quantile(.25) # 1º Quartil
Q3 = dados.Valor.quantile(.75) # 3º Quartil
IIQ = Q3 - Q1
LI = Q1 - 1.5 * IIQ
LS = Q3 + 1.5 * IIQ

# Removendo Outliers
dados_new = dados[(dados.Valor >= LI) & (dados.Valor <= LS)]

#Gráfico depois
print('Gráfico depois de remover outliers\n')
plt.rc('figure', figsize = (12,4))
plt.boxplot(dados_new.Valor, vert=True)
plt.title("Valor de Locação de Imóveis", loc="center", fontsize=18)
plt.ylabel("Valor de Locação")
plt.show()

#Gráficos Juntos
area = plt.figure()
g1 = area.add_subplot(1, 2, 1)
g2 = area.add_subplot(1, 2, 2)
g1.boxplot(dados['Valor'])
g2.boxplot(dados_new['Valor'])
g1.set_title("Valor de Locação Com Outlier", loc="center", fontsize=14)
g2.set_title("Valor de Locação Sem Outlier", loc="center", fontsize=14)
plt.show()

area.savefig('files/antes_depois_outlier.png', dpi = 300, bbox_inches = 'tight')