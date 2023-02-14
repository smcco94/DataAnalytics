import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Lê arquivo csv
notas = pd.read_csv("../files/ratings.csv")
filmes = pd.read_csv("../files/movies.csv")
#Renomeia Colunas
notas.columns = ["UsuarioID","FilmeID","Nota","Momento"]
filmes.columns = ["FilmeID","Título","Gênreo"]
#Uso de query
notas.query("FilmeID==2").Nota.mean()
#Agrupando por filmee e tirando média das notas
notas_por_filme = notas.groupby("FilmeID").mean()["Nota"]
#Gerando histograma
notas_por_filme.plot(kind='hist')
sns.boxplot(x=notas_por_filme)
sns.distplot(x=notas_por_filme, bins=20) #Bins define range em x, não necessita utilizar
#Descrevendo os dados
notas_por_filme.describe()
#matplot diretamente
plt.hist(notas_por_filme)
plt.title("Hitograma Média dos Filmes")