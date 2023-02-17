import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tmdb = pd.read_csv('../files/tmdb_5000_movies.csv')
#verificando linguas originais dos filmes
tmdb.original_language.unique()
#contando a quantidade de linguas
tmdb.original_language.value_counts()
#transformando em um dataframe e resetando index
cont_lingua = tmdb.original_language.value_counts().to_frame().reset_index()
cont_lingua.columns = ["original_language","total"]
#Plotando baixo nivel
sns.barplot(x="original_language",y="total",data = cont_lingua)
#Plotando alto nivel
sns.catplot(x = "original_language", kind="count", data = tmdb)
#Criando historio Ingles X Resto
total_por_lingua = tmdb["original_language"].value_counts()
total_geral = total_por_lingua.sum()
total_de_ingles = total_por_lingua.loc["en"]
total_do_resto = total_geral - total_de_ingles
dados = {
    'lingua' : ['ingles','outros'],
    'total' : [total_de_ingles, total_do_resto]
}
dados = pd.DataFrame(dados)
sns.barplot(data = dados, x = 'lingua', y = 'total')
#criando visualização sem ser lingua inglesa
not_ing = tmdb.query("original_language != 'en'")
#Plotando com aspect, que altera largura da caixa, e height altura e alterando cor pallete
# utilizando no pallete _r, inverte a cor (se for do tipo gradiente), exemplo: pallete="blues_r"
sns.catplot(x = "original_language", kind="count", data = not_ing, aspect = 2, palette="magma_r",
            order = not_ing.original_language.value_counts().index)