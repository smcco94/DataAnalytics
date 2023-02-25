import pandas as pd # type: ignore
import numpy as np # type: ignore

dados = pd.read_csv('../files/dados.csv', sep=',')

################## Conceitos

### População
# Conjunto de todos os elementos de interesse em um estudo. Diversos elementos podem compor uma população, 
# por exemplo: pessoas, idades, alturas, carros etc.
# Com relação ao tamanho, as populações podem ser limitadas (populações finitas) ou ilimitadas (populações infinitas).

### Populações finitas
# Permitem a contagem de seus elementos. Como exemplos temos o número de funcionário de uma empresa, 
# a quantidade de alunos em uma escola etc.

### Populações infinitas
# Não é possível contar seus elementos. Como exemplos temos a quantidade de porções que se pode extrair da água do 
# mar para uma análise, temperatura medida em cada ponto de um território etc.

    # Quando os elementos de uma população puderem ser contados, porém apresentando uma quantidade muito grande, 
    # assume-se a população como infinita.

### Amostra
# Subconjunto representativo da população.

# Os atributos numéricos de uma população como sua média, variância e desvio padrão, são conhecidos como parâmetros. 
# O principal foco da inferência estatística é justamente gerar estimativas e testar hipóteses sobre os parâmetros 
# populacionais utilizando as informações de amostras.

################## Quando utilizar uma amostra

### Testes destrutivos
# Estudos onde os elementos avaliados são totalmente consumidos ou destruídos. 
# Exemplo: testes de vida útil, testes de segurança contra colisões em automóveis.

### Resultados rápidos
# Pesquisas que precisam de mais agilidade na divulgação. 
# Exemplo: pesquisas de opinião, pesquisas que envolvam problemas de saúde pública.

### Custos elevados
# Quando a população é finita mas muito numerosa, o custo de um censo pode tornar o processo inviável.

##### Amostragem Aleatória Simples *********** EXEMPLOS *************

# É uma das principais maneiras de se extrair uma amostra de uma população. 
# A exigência fundamental deste tipo de abordagem é que cada elemeto da população tenha as mesmas chances de 
# ser selecionado para fazer parte da amostra.

# Verificando média da população e quantidade de itens em dados
dados.shape[0]
dados.Renda.mean()
# Retirando amostra, 100 itens
amostra = dados.sample(n = 100, random_state=101)
amostra.Renda.mean()
# Verificando amostra sexo
dados.Sexo.value_counts(normalize=True)
amostra.Sexo.value_counts(normalize=True)

##### Outras Amostras

# Amostragem Estratificada
    # É uma melhoria do processo de amostragem aleatória simples. 
    # Neste método é proposta a divisão da população em subgrupos de elementos com características similares, ou seja, 
    # grupos mais homogêneos. Com estes subgrupos separados, aplica-se a técnica de amostragem aleatória simples 
    # dentro de cada subgrupo individualmente.
# Amostragem por Conglomerados
    #Também visa melhorar o critério de amostragem aleatória simples. 
    # Na amostragem por conglomerados são também criados subgrupos, porém não serão homogêneas como na amostragem estratificada. 
    # Na amostragem por conglomerados os subgrupos serão heterogêneos, onde, em seguida, 
    # serão aplicadas a amostragem aleatória simples ou estratificada.
    # Um exemplo bastante comum de aplicação deste tipo de técnica é na divisão da população em grupos territoriais, 
    # onde os elementos investigados terão características bastante variadas.