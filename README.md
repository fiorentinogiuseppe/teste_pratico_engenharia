# Teste pratico engenharia de dados - Intelivix
Meu teste prático passo a passo reproduzível para o time de "Engenharia de Dados" d@ [Intelivix](https://intelivix.com/). 

Para executar este teste é necessário possui o Docker e o docker-compondo. 
Além disso é necessário instalar os requisitos. Assim indico criar um ambiente virtual 
e instalar os requisitos usando o pip da seguinte maneira:

 ```
pip install -r requirements.txt
```

:warning: Todos os comandos que serão descritos, em sua maioria, é para ser executado 
no terminal do GNU/LINUX :penguin: . Além disso não é necessário esta na pasta home do projeto 
para executar os códigos.

### Organização do repositório
Este repositório esta organizado da seguinte maneira. ~~indico consultar caso se complique na organização, pois
os diretorios e arquivos estao todos comentados~~: 
```
.
├── data_file - diretorio dos links de datasets para download
│   └── datasets.txt - links de datasets para download
├── datasets - diretorio dos datasets utilizados
│   └── dataset-0.json - dataset utilizado
├── doc - documentos utilizados
│   └── Help.me - links utilizados para consulta
├── dockers - ditetorio de dockers
│   └── docker-compose.yml - docker-compose utilizado
├── dumps - dumps/exports/exportação da base SQL
│   ├── andamentos.csv
│   ├── etiquetas.csv
│   └── processos.csv
├── modelo_de_dados - modelagem ER do banco SQL baseado no NoSQL
│   └── ER.jpg
├── notebooks - notebooks utilizados
│   └── teste_01.ipynb
├── OBJETIVOS.md - Os objetivos a serem feitos
├── README.md - Documentação explicativa do projeto
├── requirements.txt - Requerimentos python
├── src - Source code diretório
│   ├── __init__.py
│   ├── intUtilx - diretório com os uteis a sere utilizados
│   │   ├── download_datasets.py
│   │   ├── models.py
│   │   │    
│   │   └── utils.py
│   ├── q_1.py
│   ├── q_2.py
│   ├── q_31.py
│   ├── q_32.py
│   ├── q_33.py
│   └── q_4.py
├── tempos_de_execucao.txt - Arquivo contendo o tempo de execução de cada questão
└── test - Diretorio de teste
```

## Data

Os dados usados aqui foram herdados do
[teste pratico de engenharia de dados](https://github.com/intelivix/teste_pratico_engenharia) 
d@ Intelivix.
Os arquivos são jsons com dados referentes à processos e estão n diretório 
[./datasets](https://github.com/fiorentinogiuseppe/teste_pratico_engenharia/tree/master/datasets). 

:warning: Neste teste foi utilizado apenas o **dataset-0.json**, pois não estava sendo
possível realizar o download dos outros datasets por problemas referentes à perda de conexão
com o *peer*.


### *"Bring up"* o ambiente
Pensando na replicabilidade do teste foi utilizado o docker-compose como forma de conteinerização
das principais ferramentas tornando simples a replicabilidade.

Em um terminal (para ajudar na visualização e para não se perder indico utilizar o 
[terminator](https://launchpad.net/terminator)) digite os seguintes comandos: 

```
cd dockers
docker-compose up
```

Assim teremos os seguintes ambiente *em pé*:
* MongoDB - Nossa base dados NoSQL
    * username: intelivix
    * password: Testeintelivix2020!
    * port: 27017
    * admin username: root
    * admin password: Testeintelivix2020!
* Mongo Express - Interface gráfica para ajudar na visualização dos dados NoSQL
    * url : http://localhost:8081/
    * username: root
    * password: Testeintelivix2020!
* Postgres - Nossa base dados SQL
    * username: postgres
    * password: Testeintelivix2020!
* Pgadmin -  Interface gráfica para ajudar na visualização dos dados SQL
    * url: http://localhost:16543/
    * username: fiorentinogiuseppebcc@gmail.com
    * password: Testeintelivix2020!

## Questões comentadas
Após todo o ambiente configurado e entendido a organização do repositório podemos iniciar as
questões

![](/tmp/incio_da_caminhada.png)

### Questão 1
* :question: <mark>Carregar uma das bases de dados listadas acima em um banco de dados MongoDB.</mark>
    * :grey_exclamation: Para realizar o objetivo simplesmente criei a conexão com o mongo e carreguei o json em 
    memoria. Após termos a nossa conexão e os dados carregados utilizei o método do mongo "insert_many" para inserir 
    todos os dados de uma única vez. Fechando a conexão ao terminar.

Para executar o script execute o comando ~~em outro terminal já que o anterior esta rodando nossos
dockers~~
 ```
python src/q_1.py
```

### Questão 2
* <mark>Responder as seguintes consultas</mark>:
    * :question: Contagem total dos processos.
        * :grey_exclamation: Como os dados estavam no mongo utilizei as consultas do mongodb.
        Para este problema apenas contei os documentos com a query **{}** como se fosse o **select everything** do SQL
    * :question: Contagem total dos andamentos.
        * :grey_exclamation: Neste não utilize uma consulta NoSQL. Localizei todos os dados e fiz um **loop** 
        por cada andamento dentro do processo contando-o.
    * :question: Contagem de processos por estado.
        * :grey_exclamation: Voltei para as consultas NoSQL e fiz um **group by** por estado e um **count**
        em tudo dentro do group e ordenei ascendentemente.
    * :question: Contagem de juízes que começam com 'S'.
        * :grey_exclamation: Fiz um count_documents utilizando o regex para nomes de juiz que começa com **S**
    * :question: Contagem de etiquetas mais comuns.
        * :grey_exclamation: Busquei todos as etiquetas utilizando o mongo e após isso usei o **COUNTER** do python
        para contar as ocorrencias unicas das etiquetas.

Para executar o script execute o comando ~~em outro terminal já que o anterior esta rodando nossos
dockers~~
 ```
python src/q_2.py
```

### Questão 3
Dado que o objetivo principal é ler os dados a partir do MongoDB, que é uma base NoSQL,
transformá-los e carregar o resultado em uma tabela do PostgreSQL, que como própiro nome diz é uma base SQL. Porém 
para isso precisamos destrinchar o documento tentando mapear para o modelo ER ~~quase uma engenharia reversa 
de base de dados~~. Com isso em mente a tentativa do mapeamento gerou a imagem a seguir:

   ![Modelo de base](/modelo_de_dados/ER.jpg)

Com o modelo mapeado as tabelas do PostgreSQL foram construidas

#### Questão 3-1
* :question: Gerar 2 modelos (Processo e Andamento) usando SQLAlchemy. Inferir os campos através do esquema apresentado 
acima. O candidato tem liberdade para criar novos campos para lhe ajudar nas tarefas.
    * :grey_exclamation: Com o modelo em mãos foi só desenvolver as classes no [models.py](https://github.com/fiorentinogiuseppe/teste_pratico_engenharia/blob/master/src/intUtilx/models.py) 
    representando cada classe uma tabela. Contendo informações de cada um dos campos, além da sua relação, one-to-may 
    entre outras. Após criar as classes/modelos é só importar no 
    [q_31.py](https://github.com/fiorentinogiuseppe/teste_pratico_engenharia/blob/master/src/q_31.py) 
    para podermos materializar as tabelas na base utilizando o método **.create()**. 
    
Para executar o script execute o comando ~~em outro terminal já que o anterior esta rodando nossos dockers~~
 ```
python src/q_31.py
```

#### Questão 3-2
*   Realizar as transformações abaixo:
    * :question: Deixar somente o primeiro e último nome dos Juízes.
        * :grey_exclamation: 
    * :question: Remover todos os andamentos cuja data for anterior a data de distribuição.
        * :grey_exclamation:
    * :question: Modificar os npus que não possuam um ano entre 1980 e 2018 para o ano 2000.
        * :grey_exclamation:
    * :question: Remover todas as palavras que comecem com a letra 'r' dos textos dos andamentos.
        * :grey_exclamation:
    * :question: Adicionar um campo inteiro no modelo de Processo com a quantidade de andamentos 
    (somente os válidos que já foram transformados).
        * :grey_exclamation:
    * :question: Adicionar um campo booleano no modelo de Andamento que verifique se a palavra cinema esta no texto.
        * :grey_exclamation:

Para executar o script execute o comando ~~em outro terminal já que o anterior esta rodando nossos
dockers~~
 ```
python src/q_32.py
```

#### Questão 3-3
* Responder as seguintes consultas pós-processamento:
    * :question: Qual o total de processos? Qual o total de andamentos?
        * :grey_exclamation: 
    * :question: Qual processo possui mais andamentos?
        * :grey_exclamation: 
    * :question: Quais andamentos possuem mais caracteres? Quais são os seus processos?
        * :grey_exclamation: 
    * :question: Qual andamento mais antigo com o termo "cinema"?
        * :grey_exclamation: 
    * :question: Qual processo possui o maior número formado pelos seus 6 primeiros números do seu npu?
        * :grey_exclamation: 
    * :question: Qual mês/ano foram capturados mais processos para cada "spider"?
        * :grey_exclamation: 

Para executar o script execute o comando ~~em outro terminal já que o anterior esta rodando nossos
dockers~~
 ```
python src/q_33.py
```

### Questão 4
* :question: Ao final exportar as tabelas do banco de dados PostgreSQL para um arquivo chamado report.csv (delimitador de texto 
' " ', separador ' | ').
    * :grey_exclamation: fiz um select everything nas tabelas e fui salvando linha por linha em um arquivo csv.
    Com delimitador '|' e aspas '"' (QUOTE_NONNUMERIC).

Para executar o script execute o comando ~~em outro terminal já que o anterior esta rodando nossos
dockers~~
 ```
python src/q_4.py
```

## Tempo de execução de cada uma das questões
### Questão 1
```
real    0m2,218s
user    0m0,624s
sys     0m0,156s
```
### Questão 2
```
real    0m0,609s
user    0m0,283s
sys     0m0,103s
```
### Questão 3
#### Questão 3-1
```
real    0m1,232s
user    0m0,331s
sys     0m0,052s
```
#### Questão 3-2
```
real    36m10,017s
user    2m33,443s
sys     0m17,256s
```
#### Questão 3-3
```
real    0m0,325s
user    0m0,180s
sys     0m0,030s
```
### Questão 4
```
real    0m1,500s
user    0m0,998s
sys     0m0,083s
```

