import pandas as pd

#importando arquivos
aluguel = pd.read_csv('files/aluguel.csv', sep=';')

#criando lista d etipo de residencias
list(aluguel['Tipo'].drop_duplicates())
residencial = ['Quitinete','Casa','Apartamento','Casa de Condomínio','Casa de Vila']

#Responde true || false para a condição, neste caso, se está dentro dos itens da variavel residencial
aluguel['Tipo'].isin(residencial)

#seleciona do df aluguel os itens true do tipo de residencial
aluguel_residencial = aluguel[aluguel['Tipo'].isin(residencial)]

#Organizando o index
aluguel_residencial.index = range(aluguel_residencial.shape[0]) # type: ignore
aluguel_residencial.columns.name = 'ID'

#exportando como CSV
aluguel_residencial.to_csv('files/aluguel_residencial.csv', sep=';', index = False)

################ EXTRA ####################
#ordenando por uma coluna
# poderia usar 'inplace = True' pra ja aplicar a ordenação
aluguel_residencial.sort_values('Valor', ascending=False)