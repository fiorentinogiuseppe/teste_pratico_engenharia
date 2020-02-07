# Teste pratico engenharia de dados - Intelivix
Meu teste prático passo a passo reproduzível para o time de "Engenharia de Dados" d@ [Intelivix](https://intelivix.com/). 

Para executar este teste é necessário possui o Docker e o docker-compondo. 
Além disso é necessário instalar os requisitos. Assim indico criar um ambiente virtual 
e instalar os requisitos usando o pip da seguinte maneira:

 ```
pip install -r requirements.txt
```

:warning: Todos os comandos que serão descritos, em sua maioria, é para ser executado 
no terminal do GNU/LINUX :penguin: 

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
Após tudo o ambiente configurado e entendido a organização do repositório podemos iniciar as
questões

![](/tmp/incio_da_caminhada.png)

### Questão 1
* :question: <mark>Carregar uma das bases de dados listadas acima em um banco de dados MongoDB.</mark>
    * :grey_exclamation: Para realizar o objetivo simplesmente criei a conexão com o mongo e carreguei o json em 
    memoria. Após termos a nossa conexão e os dados carregados utilizei o método do mongo "insert_many" para inserir 
    todos os dados de uma única vez. Fechando a conexão ao terminar.


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
### Questão 3

![Modelo de base](/modelo_de_dados/ER.jpg)


#### Questão 3-1
#### Questão 3-2
#### Questão 3-3
### Questão 4
* :question: Ao final exportar as tabelas do banco de dados PostgreSQL para um arquivo chamado report.csv (delimitador de texto 
' " ', separador ' | ').
    * :grey_exclamation: fiz um select everything nas tabelas e fui salvando linha por linha em um arquivo csv.
    Com delimitador '|' e aspas '"' (QUOTE_NONNUMERIC).

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

