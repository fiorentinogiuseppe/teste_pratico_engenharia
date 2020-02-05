from sqlalchemy import create_engine
engine = create_engine('postgresql+psycopg2://postgres:Testeintelivix2020!@localhost:15432/postgres')

engine.execute('INSERT INTO person (name, balance) VALUES (:name, :balance)', name = 'Joe', balance = 100)