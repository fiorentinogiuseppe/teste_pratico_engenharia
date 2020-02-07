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
Este repositório esta organizado da seguinte maneira
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

## Questões
### Questão 1
### Questão 2
### Questão 3
#### Questão 3-1
#### Questão 3-2
#### Questão 3-3
### Questão 4
