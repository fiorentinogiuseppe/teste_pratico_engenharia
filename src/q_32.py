from sqlalchemy import MetaData, Table
from pymongo import MongoClient
from copy import deepcopy
import re
from datetime import datetime
from intUtilx.utils import create_connection, create_engine_sql, close_client


# -------------------- Insert Functions --------------------
def insert_db_etiquetas(items):
    rslt_id = []
    metadata = MetaData()
    metadata.reflect(engine, only=['etiquetas'])
    table = Table('etiquetas', metadata, autoload=True, autoload_with=engine)
    for item in items:
        id = engine.execute(table.insert(), {'cor':item})
        rslt_id.append(id.inserted_primary_key[0])
    return rslt_id


def insert_db_processos(item):
    metadata = MetaData()
    metadata.reflect(engine, only=['processos'])
    table = Table('processos', metadata, autoload=True, autoload_with=engine)
    del item['_id']
    id = engine.execute(table.insert(), item)
    return id.inserted_primary_key[0]


def insert_db_andamentos(itens, id_processo, ids_etiquetas):
    metadata = MetaData()
    metadata.reflect(engine, only=['andamentos'])
    table = Table('andamentos', metadata, autoload=True, autoload_with=engine)
    id_cont_etiquetas = 0
    for item in itens:
        item['processos_id'] = id_processo
        item['etiquetas_id'] = ids_etiquetas[id_cont_etiquetas]
        engine.execute(table.insert(), item)
        id_cont_etiquetas += 1


# -------------------- Mining Functions --------------------
def edit_juiz(juiz):
    """

    Parameters
    ----------
    juiz

    Returns
    -------

    """
    part_name = juiz.split(" ")
    return ' '.join([part_name[0], part_name[-1]])


def edit_npu(npu):
    """

    Parameters
    ----------
    npu

    Returns
    -------

    """
    str = npu.split('.')
    data = int(str[1])
    if data < 1980 or data > 2018:
        str[1] = '2000'
    return '.'.join(str)


def miningData(item):
    processos = get_processos(item)

    andamentos = get_andamentos(item, item['data_distribuicao'])
    processos['quantidade_andamentos'] = len(andamentos)
    if len(andamentos):
        return processos, andamentos, get_etiquetas(item)
    return processos, andamentos, None


# -------------------- Get Functions --------------------
def get_processos(item):
    """

    Parameters
    ----------
    item

    Returns
    -------

    """
    item = deepcopy(item)
    item.pop('andamentos', None)
    item['juiz'] = edit_juiz(item['juiz'])
    item['npu'] = edit_npu(item['npu'])
    return item


def get_andamentos(item, data_de_distribuicao):
    """

    Parameters
    ----------
    item
    data_de_distribuicao

    Returns
    -------

    """
    item = deepcopy(item)
    return_data = []
    for i in item['andamentos']:
        delta = datetime.strptime(data_de_distribuicao, "%Y-%m-%dT%H:%M:%SZ") - datetime.strptime(i['data'], "%Y-%m-%dT%H:%M:%SZ")
        if delta.total_seconds() < 0:
            i.pop('etiquetas', None)
            # start with space+r+word
            # so por garantia removi "r "
            i['texto'] = re.sub(r'\b[rR]\w+', "", i['texto']).replace("r ","")

            if i['texto'].find('cinema') != -1:
                i['bool_cinema'] = True
            else:
                i['bool_cinema'] = False
            return_data.append(i)
    return return_data


def get_etiquetas(item):
    """

    Parameters
    ----------
    item

    Returns
    -------

    """
    etiquetas = []
    for i in item['andamentos']:
        etiquetas.append(i['etiquetas'])
    return etiquetas


engine = create_engine_sql()
my_collection, client = create_connection()

id_andamentos = None
for item in my_collection.find():
    processos, andamentos, etiquetas= miningData(item)
    id_processo = insert_db_processos(processos)
    if etiquetas is not None and len(andamentos) > 0:
        ids_etiquetas = insert_db_etiquetas(etiquetas)
        insert_db_andamentos(andamentos, id_processo, ids_etiquetas)

close_client(client)

