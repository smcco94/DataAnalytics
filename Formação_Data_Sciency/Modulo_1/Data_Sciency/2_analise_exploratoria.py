import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#Lê arquivo csv
notas = pd.read_csv("../files/ratings.csv")
filmes = pd.read_csv("../files/movies.csv")
#Renomeia Colunas
notas.columns = ["UsuarioID","FilmeID","Nota","Momento"]
filmes.columns = ["FilmeID","Título","Gênreo"]
#Uso de query
notas.query("FilmeID==2").Nota.mean()
#Agrupando por filmee e tirando média das notas
notas_por_filme = notas.groupby("FilmeID").mean()["Nota"]
votos_por_filme = notas.groupby("FilmeID").count()["UsuarioID"]
#Gerando histograma
notas_por_filme.plot(kind='hist')
sns.boxplot(x=notas_por_filme)
sns.distplot(x=notas_por_filme, bins=20) #Bins define range em x, não necessita utilizar
#Descrevendo os dados
notas_por_filme.describe()
#matplot diretamente
plt.hist(notas_por_filme)
plt.title("Hitograma Média dos Filmes")

#############################################################################################################################
# Desafio. Criar Novo dataframe agrupados com ID com contagem de usuario, media de voto e tantar calcular a media ponderada #
#############################################################################################################################

# numpy - media pondera
media = np.average(notas_por_filme)
ponderada = np.average(notas_por_filme, weights=votos_por_filme)

# pandas juntando series
geral = pd.merge(votos_por_filme,notas_por_filme, how='inner', on='FilmeID')

# Criar coluna calculada para validar filmes com média acima da ponderada
validacao = notas_por_filme / ponderada # type: ignore

# Juntou a coluna calculada ao dataframe geral
classificacao = pd.merge(geral,validacao, how='inner', on='FilmeID')

# filtrou filmes com média acima da ponderada
class_filtro = classificacao.query('Nota > 1')

# Criou uma coluna calculada para criterio de ordenação em ralação ao peso (validação e Qtd de votos)
criterio = class_filtro.Nota * class_filtro["QTD Votos"]

# Juntou a coluna de criterio ao dataframe filtrado
final = pd.merge(class_filtro,criterio.to_frame(), how='inner', on='FilmeID')

# Renomeou as colunas
final.columns = ["QTD_Votos", "Média_Notas", "Validação","Criterio"]

# ordenou o dataframe em relação ao criterio
class_ord = final.sort_values(by=["Criterio"], ascending=False)

#descobrindo filme com maior votos, top 10
Tier10 = pd.merge(class_ord,filmes, how='left',on='FilmeID').head(10)