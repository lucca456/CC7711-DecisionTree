# CC7711-DecisionTree
# CC7711-DecisionTree

# Árvore de Decisão - bank.arff

A base de dados bank.arff representa os atributos de uma campanha de marketing bancário e se referem a informações de contato de clientes potenciais. Cada linha representa uma pessoa que foi contatada e possui informações como idade, emprego, estado civil, educação, histórico de crédito, etc. O último atributo "subscribed" indica se essa pessoa assinou ou não um produto bancário após a campanha. Esses dados podem ser usados para desenvolver modelos de aprendizado de máquina para prever se um cliente potencial assinará ou não um produto bancário.

## As informações dos atributos são as seguintes:

**idade:** idade do cliente 

**profissão:** categoria profissional do cliente 

**estado civil:** estado civil do cliente 

**educação:** nível de educação do cliente default: se o cliente tem crédito em default (sim ou não) 

**saldo:** média anual do saldo do cliente em euros 

**habitação:** se o cliente tem empréstimo habitacional (sim ou não) 

**empréstimo:** se o cliente tem empréstimo pessoal (sim ou não) 

**contato:** método de contato (celular, telefone ou desconhecido) 

**dia:** dia do mês do último contato
 
**mês:** mês do último contato 

**duração:** duração do último contato em segundos 

**campanha:** número de contatos realizados durante esta campanha e para este 
cliente 
**pdays:** número de dias que se passaram após o último contato do cliente em uma campanha anterior (numérico; -1 significa que o cliente não foi contatado anteriormente) 

**anterior:** número de contatos realizados antes desta campanha e para este cliente
 
**poutcome:** resultado da campanha de marketing anterior (sucesso, fracasso, desconhecido)

## A variável alvo (resultado) é:

**inscrito:** se o cliente se inscreveu em um depósito a prazo (sim ou não)

### Árvore de Decisão
![Figure_2.png](https://github.com/lucca456/CC7711-DecisionTree/blob/main/Figure_2.png?raw=true)

Uma árvore de decisão é uma estrutura de dados que representa um conjunto de decisões e suas possíveis consequências. É uma técnica de modelagem usada em ciência de dados e aprendizado de máquina, que usa uma árvore para representar um conjunto de regras de decisão e suas possíveis saídas. A árvore é construída a partir de um conjunto de dados de treinamento e pode ser usada para prever a classe de novos dados com base em seus atributos.

### Matriz de Confusão
![Figure_1.png](https://github.com/lucca456/CC7711-DecisionTree/blob/main/Figure_1.png?raw=true)
Existem algumas razões pelas quais a matriz de confusão pode apresentar inconsistências nos dados, mesmo que os valores fora da diagonal não sejam zero:

A distribuição das classes não foi uniforme, a matriz de confusão pode não refletir adequadamente o desempenho do modelo. Por exemplo, se a maioria das observações pertencer a uma classe específica, o modelo pode ser viésado para prever essa classe com mais frequência, o que pode levar a falsos positivos e falsos negativos.