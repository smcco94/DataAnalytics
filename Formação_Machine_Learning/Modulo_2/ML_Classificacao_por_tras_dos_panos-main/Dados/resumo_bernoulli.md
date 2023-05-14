O teorema de Bayes é uma fórmula utilizada para calcular a probabilidade de um evento ocorrer sabendo que um outro evento, chamado de condicionante, já ocorreu, denominado probabilidade condicional. Sua notação é dada por P(A|B), que significa a probabilidade de A dado que B já aconteceu e é definido pela seguinte equação:

alt text: Fórmula: Probabilidade de A dado B é igual ao quociente entre dois termos. No numerador temos a probabilidade de B dado A multiplicado pela probabilidade de A. No denominador temos  dividido pela probabilidade de B.

Onde:

P(B|A): probabilidade de B acontecer dado que A já aconteceu;
P(A): probabilidade de A acontecer;
P(B): probabilidade de B acontecer.
Falando dessa forma, pode ficar complicado de visualizar na prática o que isso realmente significa. Como o teorema de Bayes envolve probabilidade, pode ser aplicado a inúmeros contextos. Vamos utilizar aqui um exemplo envolvendo a área da saúde, mas o teorema poderia ser utilizado em outras áreas. Considere o exemplo:

Covid-19 (5%)	Sem Covid-19 (95%)
Teste positivo	85%	10%
Teste Negativo	15%	90%
Primeiramente, vamos entender o que está na tabela. Sabemos, através de pesquisas realizadas anteriormente, que há uma probabilidade de 5% de ter Covid-19. Consequentemente, há uma probabilidade 95% de não ter. Quem tem a doença está na coluna “Covid-19 (5%)” e possui uma probabilidade de 85% de testar positivo e 15% de negativo. Já quem não tem está na coluna “Sem Covid-19 (95%)” e possui uma probabilidade de 10% de testar positivo e 90% de negativo.

De posse dessas informações, vamos responder à pergunta: quais as chances de ter Covid-19 dado que o teste deu positivo?

Evento A: ter Covid-19
Evento B: positivo no teste (evento condicionante)
Utilizando a fórmula apresentada anteriormente, precisamos definir algumas probabilidades, como:

P(B|A): probabilidade do teste ser positivo dado que a pessoa tem Covid-19, que é de 85% ou 0.85, de acordo com a tabela.
P(A): probabilidade de ter covid-19. Observando a tabela, temos que é de 5%, ou 0.05.
P(B): a probabilidade do teste ser positivo.
A P(B) não conseguimos encontrar diretamente na tabela, pois a probabilidade do teste ser positivo pode acontecer quando a pessoa testada possui a doença ou não (chamado também de complementar). Logo, a probabilidade P(B) pode ser calculada como:

alt text: Fórmula: Probabilidade de B é igual a probabilidade de B dado A multiplicado pela probabilidade de A somados à probabilidade de B dado A complementar multiplicado pela probabilidade de A complementar. A complementar é representado por A elevado a C.

P(B|AC): probabilidade do teste ser positivo dado que a pessoa não possui Covid-19, que é 10% ou 0.1
P(AC): probabilidade da pessoa não ter Covid-19, que é 95% ou 0.95.
Novamente, as informações acima foram retiradas diretamente da tabela. Pronto, agora temos todas as informações que precisamos. Colocando na equação temos que:

alt text: Fórmula: Probabilidade de B é igual a 0.85 multiplicado por 0.05 somados a 0.1 multiplicado por 0.95 que é igual a 0.1375.

Jogando esses valores na primeira equação, temos que:

alt text: Fórmula: Probabilidade de A dado B é igual a probabilidade de B dado A multiplicado pela probabilidade de A dividido pela probabilidade de B que é igual a 0.85 multiplicado por 0.05. dividido por 0.1375 que é igual a 0.31.

Logo, as chances de ter Covid-19, dado que o teste deu positivo, são de 31%.