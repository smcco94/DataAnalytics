import pandas as pd # type: ignore
from scipy.special import comb # type: ignore
from scipy.stats import binom # type: ignore

dados = pd.read_csv('../files/dados.csv',sep=',')

#Distribuição Binomial / Booleano / 2 respostas possíveis
# Características
# 1. Realização de n ensaios idênticos.
# 2. Os ensaios são independentes.
# 3. Somente dois resultados são possíveis, exemplo: Verdadeiro ou falso; Cara ou coroa; Sucesso ou fracasso.
# 4. A probabilidade de sucesso é representada por p e a de fracasso por 1-p=q. Estas probabilidades não se modificam de ensaio para ensaio.

#Variaveis
# n = Número de ensaios
# p = probabilidade de sucesso
# q = probabilidade de fracasso
# k = qual o total de eventos que desaja-se obter sucesso

comb_loteria = comb(60,6) # mega sena, 60 numeros para 6 marcações. Assim calculamos o numero de combinações possíveis
prob = 1 / comb_loteria # prob indica probabilidade de acertar na mega-sena

# First Quiz
comb_quiz = comb(25,20) # Combinações Possíveis = Espaço Amostral
prob_quiz = 1 / comb_quiz

############# EXEMPLO Concurso
# Em um concurso para preencher uma vaga de cientista de dados temos um total de 10 questões de múltipla escolha 
# com 3 alternativas possíveis em cada questão. Cada questão tem o mesmo valor. Suponha que um candidato resolva 
# se aventurar sem ter estudado absolutamente nada. Ele resolve fazer a prova de olhos vendados e chutar todas as resposta. 
# 
# 1 Questão: Assumindo que a prova vale 10 pontos e a nota de corte seja 5, obtenha a probabilidade deste candidato
# acertar 5 questões.
# 
# 2 Questão: A probabilidade deste candidato passar para a próxima etapa do processo seletivo.

##############  1 Questão
# Número de ensaios
n = 10 # 10 questões
# probabilidade de sucesso
numero_alternativa_por_questao = 3
p = 1 / numero_alternativa_por_questao
# probabilidade de fracasso
q = 1 - p
# qual o total de eventos que desaja-se obter sucesso
k = 5
# Probabilidade
prob_passar = (comb(n,k) * (p ** k) * (q ** (n - k))) * 100

### Agora mesmo exercício utilizando scipy ( importar binom )
prob_scipy = binom.pmf(k,n,p)


##############  2 Questão - Para passar ele precisa acertar 5 ou 6 ou 7 ou 8 ou 9 ou 10
# Método 1 
met1 = binom.pmf(5, n, p) + binom.pmf(6, n, p) + binom.pmf(7, n, p) + binom.pmf(8, n, p) + binom.pmf(9, n, p) + binom.pmf(10, n, p)
# Método 2
met2 = binom.pmf([5, 6, 7, 8, 9, 10], n, p).sum()
# Método 3
met3 = 1 - binom.cdf(4, n, p)
# Método 4
met4 = binom.sf(4, n, p)

show = [met1,met2,met3,met4]

for i in show:
    x = 0
    print(show[x])
    x += 1

# Quiz Moeda
# Uma moeda, perfeitamente equilibrada, é lançada para o alto quatro vezes. Utilizando a distribuição binomial, 
# obtenha a probabilidade de a moeda cair com a face coroa voltada para cima duas vezes.

n_coin = 4
faces= 2
p_coin = 1 / faces
k = 2
coin = binom.pmf(k, n_coin, p_coin) # binom.pmf(Chances que deseja de sucesso, Numero de ensaios, probabilidade de sucesso)

# Quiz Dado
# Um dado, perfeitamente equilibrado, é lançado para o alto dez vezes. Utilizando a distribuição binomial, 
# obtenha a probabilidade de o dado cair com o número cinco voltado para cima pelo menos três vezes.

n_dice = 10
possibilidades = 6
p_dice = 1 / possibilidades
k = 2
dice = binom.sf(k,n_dice,p_dice) # k vai ser o numero antecessor ao  menor criterio de aceitação, neste caso k < 3 ( intervalo aberto )
# binom.cdf faz até aquele número ( intervalo fechado )

################## Exemplo Gincana
# Uma cidade do interior realiza todos os anos uma gincana para arrecadar fundos para o hospital da cidade. 
# Na última gincana se sabe que a proporção de participantes do sexo feminino foi de 60%. 
# O total de equipes, com 12 integrantes, inscritas na gincana deste ano é de 30. 
# Com as informações acima responda: Quantas equipes deverão ser formadas por 8 mulheres?

n_gincana = 12
p_gincana = 0.6
k_gincana = 8
prob_gincana = binom.pmf(k_gincana, n_gincana, p_gincana)
equipes = 30
# para calcular a média pego as equipes e multiplico pela probabilidade de ter 8 mulheres
media_binomial = equipes * prob_gincana


# Quiz Olhos Azuis
# Suponha que a probabilidade de um casal ter filhos com olhos azuis seja de 22%. 
# Em 50 famílias, com 3 crianças cada uma, quantas podemos esperar que tenham dois filhos com olhos azuis?

prob_azul = 0.22 # cada filho ter olho azul
k_azul = 2 
n_azul = 3

chance_por_familia = binom.pmf(k_azul,n_azul,prob_azul)

familias = 50
total_de_familias = familias * chance_por_familia