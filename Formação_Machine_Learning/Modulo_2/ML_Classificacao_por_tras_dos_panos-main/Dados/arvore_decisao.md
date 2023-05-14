Se você está se sentindo doente, mas não faz ideia do que possa ser, quando você vai ao médico são feitas uma série de perguntas (dor de cabeça? febre? tosse?...). Ao final da série de perguntas realizadas pelo médico é emitido um parecer informando qual a causa dos sintomas. Nessa situação apresentada foi seguido o mesmo princípio utilizado em um estimador chamado árvore de decisão.

Árvore de decisão é um dos modelos de previsão mais simples, inspirada na forma que os seres humanos tomam as decisões e tem uma alta interpretabilidade, ou seja, uma compreensão fácil dos passos que foram realizados para conseguir chegar ao resultado final. Ela pode ser utilizada tanto para modelos de regressão, que têm intuito de prever valores numéricos, quanto para modelos de classificação, que têm intuito de prever categorias.

Graficamente, a árvore de decisão pode ser representada de forma que cada uma das decisões tomadas no processo possam ser visualizadas. Seus elementos principais são os nós, ramos e folhas. A estrutura da árvore se inicia com um nó inicial, também chamado de raiz. A partir dela são traçadas ramificações, que geram novos nós e o processo se repete para os nós subsequentes até que chegue a uma folha, que se trata de um nó especial que tem a informação da resposta, sendo ela uma categoria ou um valor previsto.

Cada ramo representa uma tomada de decisão a partir de um valor ou de uma categoria das variáveis explicativas, dividindo o conjunto de dados em nós que apresentam dados com características cada vez mais similares entre si.

Para que fiquem mais compreensíveis esses conceitos, vamos a um exemplo.

alt text: Quadro com fundo cinza contendo os sintomas da Covid-19 e um fluxograma com orientações sobre o que fazer em caso de contaminação ou contato com pessoas diagnosticadas com Covid.

Na imagem de exemplo, temos uma orientação sobre Covid-19 para que as pessoas sejam direcionadas a ficarem isoladas ou não. A raiz ou nó inicial representa a pergunta se a pessoa está com sintomas de Covid-19, como aquelas perguntas realizadas pelo médico indicadas no início desse texto. A pergunta é respondida através dos ramos que partem da raiz, separando as pessoas que possuem sintomas das pessoas que não possuem sintomas.

O nó referente às pessoas que possuem sintomas se trata de um nó folha, com a decisão final de isolamento social. O nó referente às pessoas que não possuem sintomas se trata de um nó interno, que passa por um novo questionamento, criando assim novos ramos e nós. O processo se repete até que se chegue em decisões finais.

Portanto, o esquema se trata de uma Árvore de Decisão, em que é possível detectar todas as escolhas que foram feitas para se chegar às conclusões finais. O algoritmo de computador seguirá esses mesmos princípios, tomando as decisões com base nas variáveis explicativas.

Critério de divisão dos nós
Para conseguir identificar qual o melhor momento em que um nó deve ser dividido em dois ou mais subnós, o algoritmo da árvore de decisão considera alguns critérios. Os dois principais critérios de divisão usados nas árvores de decisão são:

Índice Gini
Este índice informa o grau de heterogeneidade dos dados. O objetivo dele é medir a frequência de um elemento aleatório de um nó ser rotulado de maneira incorreta. Em outros termos, esse índice é capaz de medir a impureza de um nó e ele é determinado por meio do seguinte cálculo:

alt text: Fórmula: Gini é igual a 1 menos somatório de i começando em 1 indo até K de P de i ao quadrado.

Onde:

pi representa a frequência relativa das classes em cada um dos nós;
k é o número de classes.
Se o índice Gini for igual a 0, isso indica que o nó é puro. No entanto, se o valor dele se aproxima mais do valor 1, o nó é impuro.

Entropia
A ideia básica da entropia é medir a desordem dos dados de um nó por meio da variável classificadora. Assim como o índice de Gini, ela é utilizada para caracterizar a impureza dos dados e pode ser calculada por meio da seguinte fórmula:

Alt text: Fórmula: Entropia de S, com S entre parênteses, é igual ao somatório de i iniciando em 1 até c de menos p subscrito i vezes o log 2 de p subscrito i.

Onde:

pi representa a proporção de dados no conjunto de dados (S), pertencentes à classe específica i;
c é o número de classes.