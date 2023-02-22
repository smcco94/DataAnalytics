import pandas as pd

#importando arquivos
aluguel = pd.read_csv('files/aluguel.csv', sep=';')
#Selectionando tipo de imóveis
tipo = aluguel.Tipo
#removendo duplicatas
tipo.drop_duplicates(inplace=True) #inplace = true atribui novo filtro a variavel
tipo = pd.DataFrame(tipo)# pode-se usar tipo.to_frame()
#redefinindo index
tipo.index = range(tipo.shape[0]) # type: ignore
tipo.columns.name = 'ID'


########### EXTRA ###########

# A estrutura do tipo tupla é muito semelhante à da lista. 
# A grande diferença é que a tupla é imutável, ou seja, 
# após a criação não é possível realizar alterações no seu estado. 
# Para criar tuplas no Python devemos adicionar os elementos entre parênteses e separados por vírgula.

#Criando index e colunas para demonstração
index = ['Linha' + str(i) for i in range(3)]
columns = ['Coluna' + str(i) for i in range(3)]

#Criando um dataframe
data = {'Coluna0': {'Linha0': 1, 'Linha1': 4, 'Linha2': 7},
        'Coluna1': {'Linha0': 2, 'Linha1': 5, 'Linha2': 8},
        'Coluna2': {'Linha0': 3, 'Linha1': 6, 'Linha2': 9}}

df1 = pd.DataFrame(data = data, index = index)
df2 = pd.DataFrame(data = data, index = index, columns = columns)
df3 = pd.DataFrame(data = data, index = index, columns = columns)

#Fazendo concatenação de tabelas
df1[df1 > 0] = 'A'
df2[df2 > 0] = 'B'
df3[df3 > 0] = 'C'

#Concateda uma em CIMA da outra
df4 = pd.concat([df1, df2, df3])
#Concatena uma ao LADO da outra
df5 = pd.concat([df1, df2, df3], axis = 1)