# Existem duas categorias de problemas que podem ser bem resolvidos com a utilização de Machine Learning: os de classificação e os de regressão.

## Classificação
Quando precisamos prever a qual categoria pertence uma determinada amostra, trata-se de um problema de classificação. Alguns exemplos que podemos citar são:

Prever se um(a) determinado(a) paciente está com Covid.
Se um(a) cliente está propenso(a) a desistir da compra.
Se algum(a) usuário(a) web está propenso(a) a clicar em um anúncio.
Nesses casos mencionados, a previsão se concentra em 0 ou 1 (Covid/não Covid, desistir/não desistir, clicar/não clicar) que é denominada de classificação binária, na qual existem somente duas classes. Há também casos em que a classificação se dá com mais duas classes, chamada de classificação multiclasse, como a filtragem dos e-mails em “principal”, “social”, “promoções”, “importantes” ou “fóruns”.

Entre os algoritmos de classificação podemos citar:

K-Nearest Neighbors (KNN) - https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html
Support Vector Machine (SVM) - https://scikit-learn.org/stable/modules/svm.html
Decision Tree Classifier - https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html
Random Forest Classifier- https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html

## Regressão
Quando precisamos prever um valor numérico específico, isso indica que estamos lidando com um problema de regressão. Alguns exemplos desses problemas estão relacionados à previsão de:

preços/custos futuros;
estoque;
receita futura.
Nessas situações, podemos utilizar algum modelo de regressão para realizar essas previsões e apresentar como resposta algum valor contínuo relacionado ao problema. Existem diferentes tipos de algoritmos de machine learning utilizados para resolver esse tipo de problema:

Linear Regression; - https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
Random Forest Regressor; - https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html
Support Vector Regression (SVR). - https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html