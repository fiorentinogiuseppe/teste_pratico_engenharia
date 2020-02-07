from sqlalchemy import MetaData, Table
from copy import deepcopy
import re
from datetime import datetime
from intUtilx.utils import create_connection, create_engine_sql, close_client


# -------------------- Insert Functions --------------------
def insert_db_etiquetas(items):
    """
    Insert `list` of uniques `etiquetas` in pgSQL
    Parameters
    ----------
    items: list
        Itens to be inserted in the database


    Returns
    -------
    list
        List with each id of each inserted `etiqueta`

    """
    rslt_id = []
    metadata = MetaData()
    metadata.reflect(engine, only=['etiquetas'])
    table = Table('etiquetas', metadata, autoload=True, autoload_with=engine)
    for item in items:
        id = engine.execute(table.insert(), {'cor':item})
        rslt_id.append(id.inserted_primary_key[0])
    return rslt_id


def insert_db_processos(item):
    """
    Insert `dict` of `processos` in pgSQL
    Parameters
    ----------
    item: dict
        Dictionary containing the `processos`


    Returns
    -------
    str:
        String with id of inserted `processo`

    """
    metadata = MetaData()
    metadata.reflect(engine, only=['processos'])
    table = Table('processos', metadata, autoload=True, autoload_with=engine)
    del item['_id']
    id = engine.execute(table.insert(), item)
    return id.inserted_primary_key[0]


def insert_db_andamentos(itens, id_processo, ids_etiquetas):
    """
    Insert `list` of `andamenos` in pgSQL
    Parameters
    ----------
    itens: list
        List of `andamentos` containing each of `andamento`
    id_processo: str
        String id of the `processo` that belong it .

    ids_etiquetas: list
        List id of the `etiqueta` that it belong.

    Returns
    -------
    None
    """
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
    Split juiz name and get first and last name
    Parameters
    ----------
    juiz: str
        String containing `juiz` name

    Returns
    -------
    str
        New name formatted by `FIRST_NAME+LAST_NAME`

    """
    part_name = juiz.split(" ")
    return ' '.join([part_name[0], part_name[-1]])


def edit_npu(npu):
    """
    Get npu and if it its more than 2018 or less than 1980 change your date value to `2000`
    Parameters
    ----------
    npu: str
        String containing `npu` and we want chang your date parte

    Returns
    -------
    str
        New npu

    """
    str = npu.split('.')
    data = int(str[1])
    if data < 1980 or data > 2018:
        str[1] = '2000'
    return '.'.join(str)


def mining_data(item):
    """
    Mining the json spliting in `andamento`, `processo` and `etiqueta` make the needed changes

    Parameters
    ----------
    item: json
        Json containing the main `processo` to be splited

    Returns
    -------
    json
        `Processos`json
    list
        List of `andamentos`
    list
        List of `etiquetas` if `andamentos` exist. Otherwise return None
    """

    proc = get_processos(item)
    andam= get_andamentos(item, item['data_distribuicao'])
    proc['quantidade_andamentos'] = len(andamentos)
    if len(andamentos):
        return proc, andam, get_etiquetas(item)
    return proc, andam, None


# -------------------- Get Functions --------------------
def get_processos(item):
    """
    Extract only the `processo` from others parts and alter `juiz` name and `npu` date
    Parameters
    ----------
    item: json
        Json containing the main `processo`

    Returns
    -------
    json
        `Processo` json

    """
    item = deepcopy(item)
    item.pop('andamentos', None)
    item['juiz'] = edit_juiz(item['juiz'])
    item['npu'] = edit_npu(item['npu'])
    return item


def get_andamentos(item, data_de_distribuicao):
    """
    Extract only the `andamentos` from others parts and check if these date is less than `data_de_distribuicao`
    Parameters
    ----------
    item: json
        Json containing the main `processo`
    data_de_distribuicao: str
        String representing the `data_de_distrobuicao` of the `processo`

    Returns
    -------
    list
        List of `andamentos`

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
    Extract only the `etiquetas` from others parts
    Parameters
    ----------
    itemjson
        Json containing the main `andamento`

    Returns
    -------
    list
        List of `etiquetas`
    """
    etiquetas = []
    for i in item['andamentos']:
        etiquetas.append(i['etiquetas'])
    return etiquetas


engine = create_engine_sql()
my_collection, client = create_connection()

id_andamentos = None
for item in my_collection.find():
    processos, andamentos, etiquetas= mining_data(item)
    id_processo = insert_db_processos(processos)
    if etiquetas is not None and len(andamentos) > 0:
        ids_etiquetas = insert_db_etiquetas(etiquetas)
        insert_db_andamentos(andamentos, id_processo, ids_etiquetas)

close_client(client)

