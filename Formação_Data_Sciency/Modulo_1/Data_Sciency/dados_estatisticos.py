import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


notas = pd.read_csv("../files/ratings.csv")
notas.columns = ["UsuarioID","FilmeID","Nota","Momento"]

notas_do_toy_story = notas.query("FilmeID==1")
notas_do_jumanji = notas.query("FilmeID==2")


print("Nota média do Toy Story %.2f" % notas_do_toy_story.Nota.mean())
print("Mediana do Toy Story %.2f" % notas_do_toy_story.Nota.median())
print("Desvio padrão do Toy Story %.2f" % notas_do_toy_story.Nota.std())


print("Nota média do Jumanji %.2f" % notas_do_jumanji.Nota.mean())
print("Mediana do Jumanji %.2f" % notas_do_jumanji.Nota.median())
print("Desvio padrão do Jumanji %.2f" % notas_do_jumanji.Nota.std())


sns.boxplot(x = "FilmeID", y = "Nota", data = notas.query("FilmeID in (1,2)"))


## Vale ressaltar a importancia de entender os dados, nem sempre as medidas de tendencia central vão mostrar
## o valor de uma informação sem um complemento, neste caso, o desvio pode mostrar uq mesmo com tendencias proximas
## a variação dos dados que chegaram a esse resultado pode nos mostrar pontos importantes na análise