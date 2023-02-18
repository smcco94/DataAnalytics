import pandas as pd
import html5lib
import lxml

#importando arquivos
aluguel = pd.read_csv('files/aluguel.csv', sep=';')
#dados do dataframe
aluguel.info()
#dados variaveis de campo
tipo_dados = pd.DataFrame(aluguel.dtypes, columns=['Tipo Dados'])
#nomeando index
tipo_dados.columns.name = 'Coluna'
#entendendo linha por coluna
aluguel.shape
# ||
print('A base de dados apresenta {} registros e {} variáveis'.format(aluguel.shape[0], aluguel.shape[1]))


#################### EXTRA ####################
#json
json1 = open('files/extra/aluguel.json')
print(json1.read())
json2 = pd.read_json('files/extra/aluguel.json')
#txt
txt = pd.read_table('files/extra/aluguel.txt')
#xlsx
xlsx = pd.read_excel('files/extra/aluguel.xlsx')
#HTML
html = pd.read_html('https://support.microsoft.com/pt-br/office/use-excel-built-in-functions-to-find-data-in-a-table-or-a-range-of-cells-6777ec9b-6191-426a-8d45-196ecbf2a186')
html[0]
html[1]
