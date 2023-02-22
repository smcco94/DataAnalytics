import pandas as pd

dados = pd.read_csv('files/aluguel_residencial_tratado.csv', sep=';')

#criando coluna valor bruto
dados['Valor Bruto'] = dados['Valor'] + dados['Condominio'] + dados['IPTU']

#criando variavel de valor do metro quadrado
dados['Valor m2'] = (dados['Valor']/dados['Area']).round(2)

#criando variavel de valor bruto do metro quadrado
dados['Valor Bruto m2'] = (dados['Valor Bruto']/dados['Area']).round(2)

#agregando tipos de casa em uma variavel
casa = ['Casa', 'Casa de Condomínio', 'Casa de Vila']

#executa uma condicional por linha com o método apply, agrupando o grupo de casas e o que não for guarda como apartamento
#a partir de uma função lambda
dados['Tipo Agregado'] = dados['Tipo'].apply(lambda x: 'Casa' if x in casa else 'Apartamento')


#Excluindo variavel do dataframe
#axis 1 é coluna e 0 é linha
#inplace indica para aplicar no dataframe qquando TRUE
dados.drop(['Valor Bruto', 'Valor Bruto m2'], axis = 1, inplace = True)

#exportando arquivo
dados.to_csv('files/aluguel_residencial_tratado_agregado.csv', sep=';')

#vendo frequencia por tipo
dados.Tipo.value_counts()