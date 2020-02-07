import json
from sqlalchemy import create_engine
from pymongo import MongoClient


def create_connection(config=None, database='intelivix', collection='my_collection'):
    """
    Create connection with mongodb, choose database and get chosen collection.

    Parameters
    ----------
    config: dict
        Connection settings
    database: str
        Database name
    collection: str
        Collection name

    Returns
    -------
    object
        Database Collection
    object
        Mongo Client

    """
    if config is None:
        config = {'host': 'localhost', 'port': 27017, 'username': 'root',
                  'password': 'Testeintelivix2020!', 'authSource': 'admin'}

    client_conn = MongoClient(host=config['host'],
                              port=config['port'],
                              username=config['username'],
                              password=config['password'],
                              authSource=config['authSource'])
    db = client_conn[database]
    coll = db[collection]
    return coll, client_conn


def load_json(file_path='../datasets/dataset-0.json'):
    """
    Load json file
    Parameters
    ----------
    file_path: str
        String path for the json file

    Returns
    -------
    json
        file in json format

    """

    with open(file_path) as f:
        file_json = json.load(f)

    return file_json


def close_client(client_close):
    """
    Close connection started
    Parameters
    ----------
    client_close

    Returns
    -------
    None
    """
    client_close.close()


def create_engine_sql(user='postgres', password='Testeintelivix2020!',
                      host='localhost', port=15432, database='postgres'):
    """
    Create sql connection

    Parameters
    ----------
    user: str
        Connection user
    password: str
        Connection password
    host: str
        Connection host
    port: int
        Connection port
    database: str
        Database name

    Returns
    -------
    object
        Sql engine to connection

    """
    conn_string = 'postgresql+psycopg2://{}:{}@{}:{}/{}'.format(user, password, host, port, database)
    engine = create_engine(conn_string)
    return engine
