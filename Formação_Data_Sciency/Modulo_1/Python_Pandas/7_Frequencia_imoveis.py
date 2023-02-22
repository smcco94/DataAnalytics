import pandas as pd

dados = pd.read_csv('files/aluguel_residencial.csv', sep=';')

#Selecione somente os imóveis classificados com tipo 'Apartamento'.
n1 = dados.query("Tipo=='Apartamento'").shape[0]
#Selecione os imóveis classificados com tipos 'Casa', 'Casa de Condomínio' e 'Casa de Vila'.
dados.Tipo.drop_duplicates()
n2 = dados.query("Tipo!='Apartamento' & Tipo!='Quitinete'").shape[0]
#Selecione os imóveis com área entre 60 e 100 metros quadrados, incluindo os limites.
n3 = dados.query("Area>=60 & Area<=100").shape[0]
#Selecione os imóveis que tenham pelo menos 4 quartos e aluguel menor que R$ 2.000,00.
n4 = dados.query("Quartos>3 & Valor<2000").shape[0]

print("Nº de imóveis classificados com tipo 'Apartamento' -> {}".format(n1))
print("Nº de imóveis classificados com tipos 'Casa', 'Casa de Condomínio' e 'Casa de Vila'-> {}".format(n2))
print("Nº de imóveis com área entre 60 e 100 metros quadrados, incluindo os limites -> {}".format(n3))
print("Nº de imóveis que tenham pelo menos 4 quartos e aluguel menor que R$ 2.000,00 -> {}".format(n4))