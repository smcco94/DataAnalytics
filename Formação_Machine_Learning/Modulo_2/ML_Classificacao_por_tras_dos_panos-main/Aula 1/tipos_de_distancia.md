No algoritmo KNN, para que seja feita a classificação dos registros com base nos vizinhos mais próximos, é necessário utilizar alguma medida para identificar o quão próximo o registro está dos seus vizinhos. Existem diversas medidas para se avaliar essa proximidade entre variáveis numéricas que recebem o nome de medidas de distância. Quanto maior o valor dessa medida, mais distante um elemento está do outro, ou seja, menor a similaridade entre eles.

Considere a tabela a seguir com duas observações e n variáveis para o entendimento das medidas de distância.

Observação	Variável 1	Variável 2	...	Variável n
X	X1	X2	...	Xn
Y	Y1	Y2	...	Yn

Distância Euclidiana
A medida de distância mais conhecida e mais utilizada é a distância euclidiana. Ela consiste em subtrair as coordenadas de uma observação pela outra observação, elevar ao quadrado os resultados, somar todos os valores e extrair a raiz quadrada.

alt text: Fórmula: d igual a raiz quadrada da soma de n termos: O primeiro termo é x 1 menos y 1 ao quadrado. O último termo é x n menos y n ao quadrado. Os termos intermediários da soma estão ocultos e representam os termos de x 2 a x n menos 1 e y 2 a y n menos 1.

Distância de Manhattan
Uma distância que considera apenas a soma dos módulos das diferenças entre cada par de coordenadas.

alt text: Fórmula: d igual a soma de n termos: O primeiro termo é o módulo de x 1 menos y 1. O último termo é o módulo de x n menos y n. Os termos intermediários da soma estão ocultos e representam os termos de x 2 a x n menos 1 e y 2 a y n menos 1.

Distância de Minkowski
Uma medida de distância que é a generalização de outras distâncias, como a distância euclidiana e a de Manhattan. Consiste em extrair o módulo da diferença entre cada par de coordenadas elevando o resultado a m, realizar a soma de todos os termos e, por fim, tirar a raiz m-ésima, em que m é um número qualquer. A distância euclidiana é um caso à parte quando m é igual a 2 e a distância de Manhattan é um caso à parte quando m é igual a 1.

alt text: Fórmula: d igual a raiz m ésima da soma de n termos: O primeiro termo é o módulo de x 1 menos y 1 elevado a m. O último termo é o módulo de x n menos y n elevado a m. Os termos intermediários da soma estão ocultos e representam os termos de x 2 a x n menos 1 e y 2 a y n menos 1.

Distância de Chebyshev
É uma medida de distância que considera apenas o valor máximo entre os módulos das diferenças entre as variáveis. Dessa forma, leva em consideração apenas a variável que possui a maior diferença de valores entre as duas observações.

alt text: Fórmula: d igual ao máximo entre n termos: O primeiro termo é o módulo de x 1 menos y 1. O último termo é o módulo de x n menos y n. Os termos intermediários estão ocultos e representam os termos de x 2 a x n menos 1 e y 2 a y n menos 1.

Existem diversas outras medidas de distância que podem ser calculadas e cada uma delas impacta diretamente no resultado do modelo. As distâncias apresentadas aqui podem ser utilizadas no algoritmo KNN do scikit-learn, sendo a distância de Minkowski a medida de distância padrão ao instanciar o algoritmo, como pode ser checado na documentação.

Podemos modificar a medida de distância utilizando o argumento metric da função sklearn.neighbors.KNeighborsClassifier. Com base nas medidas que foram apresentadas no texto, o parâmetro pode receber os seguintes valores:

“euclidean” para a distância euclidiana;
“manhattan” para a distância de Manhattan;
“minkowski” para a distância de Minkowski;
“chebyshev” para a distância de Chebyshev.