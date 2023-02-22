import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv('files/aluguel_residencial_tratado_agregado.csv', sep=';')

#obtemos na variavel os valores agrupados por tipo 
grupo_tipo = dados.groupby('Tipo')['Valor'] # verifica-se conteúdo utilizando grupo_tipo.groups

# Calculos para identificação de outliers
Q1 =  grupo_tipo.quantile(.25)
Q3 =  grupo_tipo.quantile(.75)
IIQ = Q3 - Q1
limite_inferior = Q1 - 1.5 * IIQ
limite_superior = Q3 + 1.5 * IIQ

#obetmos os valores dentro dos valores especificados e concatenamos gerando apenas um dataframe ao final
dados_new = pd.DataFrame()
for tipo in grupo_tipo.groups.keys():
    eh_tipo = dados['Tipo'] == tipo
    eh_dentro_limite = (dados['Valor'] >= limite_inferior[tipo]) & (dados['Valor'] <= limite_superior[tipo])
    selecao = eh_tipo & eh_dentro_limite
    dados_selecao = dados[selecao]
    dados_new = pd.concat([dados_new, dados_selecao])

#Gerando boxplot com dados tratados
print('Gráfico depois de remover outliers e agrupar por tipo\n')
plt.rc('figure', figsize = (12,4))
dados_new.boxplot(['Valor'], by='Tipo', figsize=(10,4), grid=False, vert=True)
plt.title("Valor de Locação de Imóveis Agrupado por Tipo", loc="center", fontsize=18, pad=50)
plt.ylabel("Valor de Locação")
plt.show()
