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
Este repositório está organizado da seguinte maneira. ~~indico consultar caso se complique na organização, pois
os diretórios e arquivos estão todos comentados~~: 
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
possível realizar o download dos outros *datasets* por problemas referentes à perda de conexão
com o *peer*.

Caso não tenha os dados ou deseje dados diferentes deve-se executar o script para obter todos os dados:
```
python src/download_datasets.py
```
Assim terá os dados baixados no diretório *datasets*.

### *"Bring up"* o ambiente
Pensando na replicabilidade do teste foi utilizado o docker-compose como forma de *conteinerização*
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
        em tudo dentro do group e ordenei de forma ascendente.
    * :question: Contagem de juízes que começam com 'S'.
        * :grey_exclamation: Fiz um count_documents utilizando o regex para nomes de juiz que começa com **S**
    * :question: Contagem de etiquetas mais comuns.
        * :grey_exclamation: Busquei todos as etiquetas utilizando o mongo e após isso usei o **COUNTER** do python
        para contar as ocorrências únicas das etiquetas.

Para executar o script execute o comando ~~em outro terminal já que o anterior esta rodando nossos
dockers~~
 ```
python src/q_2.py
```

### Questão 3
Dado que o objetivo principal é ler os dados a partir do MongoDB, que é uma base NoSQL,
transformá-los e carregar o resultado em uma tabela do PostgreSQL, que como próprio nome diz é uma base SQL. Porém 
para isso precisamos destrinchar o documento tentando mapear para o modelo ER ~~quase uma engenharia reversa 
de base de dados~~. Com isso em mente a tentativa do mapeamento gerou a imagem a seguir:

   ![Modelo de base](/modelo_de_dados/ER.jpg)

Com o modelo mapeado as tabelas do PostgreSQL foram construiras

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
Antes de seguir com os que foi pedido foi preciso ler toda a base MongDB e ir desmontando os dados
separando processos de andamentos de etiquetas. E com isso realizando o que será pedido a seguir e 
ir inserindo na base de dados. ~~acredito que exista um método mais rápido para inserir tudo 
ou talvez o multiprocessing do python possa ajudar a ir inserindo e assim diminua o tempo~~
*   Realizar as transformações abaixo:
    * :question: Deixar somente o primeiro e último nome dos Juízes.
        * :grey_exclamation: Para isso é só pegar o campo do processo destinado ao nome do juiz,
        split na string e pegar o primeiro o e ultimo nome.
    * :question: Remover todos os andamentos cuja data for anterior a data de distribuição.
        * :grey_exclamation: Para isso é só pegar o campo do processo destinado a data de distribuição
        junto com o campo de cada andamento e subtrair data distribuição da data do andamento e caso seja
        negativo inserir.
    * :question: Modificar os npus que não possuam um ano entre 1980 e 2018 para o ano 2000.
        * :grey_exclamation:
    * :question: Remover todas as palavras que comecem com a letra 'r' dos textos dos andamentos.
        * :grey_exclamation: No mesmo processo para obter os andamentos realiza um regex removendo
        'R[a-zA-Z0-9]', porém percebi que existia 'r ' então por via das duvidas removi também.
    * :question: Adicionar um campo inteiro no modelo de Processo com a quantidade de andamentos 
    (somente os válidos que já foram transformados).
        * :grey_exclamation: Para cada processo é um simples len(andamentos) que nos retornará este
        tipo de dado.
    * :question: Adicionar um campo booleano no modelo de Andamento que verifique se a palavra cinema esta no texto.
        * :grey_exclamation: Para cada texto do andamentos verificar, com o find, se existe a palavra.
        Caso o resultado do find() não for -1 então cinema existe e é só adicionar esse novo campo True, caso
        contrario False.

Para executar o script execute o comando ~~em outro terminal já que o anterior esta rodando nossos
dockers~~
 ```
python src/q_32.py
```

#### Questão 3-3
Com a base toda carregada no PostgreSQL as questões foram desenvolvida utilizando query SQL.
* Responder as seguintes consultas pós-processamento:
    * :question: Qual o total de processos? Qual o total de andamentos?
        * :grey_exclamation:  Um select count tudo nos dá o resultado desejado. Porém, assim como nos outros,
        no retorna um objeto nos novemos por ele utilizando um loop para *printar* nosso resultado.
    * :question: Qual processo possui mais andamentos?
        * :grey_exclamation: Inner join nos processos e andamentos com isso temos nossos processos com cada
        um dos nossos andamentos. Realizando um *group by* por id do processos e um count deste, ordenando
        em ordem decrescente a contagem e limitando por 1 a resposta da query temos nosso processo com mais
        andamento.
    * :question: Quais andamentos possuem mais caracteres? Quais são os seus processos?
        * :grey_exclamation: Select por id do andamento, processos_id e contagem de character de cada um 
        dos textos da tabela e ordenando pelo numero de character decrescente e finalmente limitando por 1
        temos nosso resultado.
    * :question: Qual andamento mais antigo com o termo "cinema"?
        * :grey_exclamation: busca a data do andamento que tem bool_cinema como true, ordena as datas 
        ascendente e limita por 1 temos a query.
    * :question: Qual processo possui o maior número formado pelos seus 6 primeiros números do seu npu?
        * :grey_exclamation: Seleciona o id e os 6 primeiros caracteres, ordenando-os de forma decrescente e limitado
        por 1 nos retorna a query.
    * :question: Qual mês/ano foram capturados mais processos para cada "spider"?
        * :grey_exclamation: Na questão mais complicada ~~na minha opinião~~tive que realizar um join a partir do resultado
        de dois selects. O primeiro select foi para obter nosso grupo de spider e numero de  month/year de forma decrescente.
        No segundo select realizamos o mesmo select contudo este está dentro de outro que irá obter o spider e o maximo
        contado das datas. Esse join por spider e máxima contagem nos da o resultado. Porém utilizando o distinct 
        obtemos apenas o primeiro resultado, pois muitas vezes existia  mais de um mês/ano em que tinha valores repartido

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
## Considerações Finais
Caso exista algum erro ou equívoco da minha parte, por favor, entrar em contato comigo pelo meu e-mail
```
fiorentinogiuseppebcc@gmail.com 
```

