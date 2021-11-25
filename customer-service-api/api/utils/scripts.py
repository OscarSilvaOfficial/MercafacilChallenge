from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from api.config import MYSQL_DATABASE_URL, POSTGRES_DATABASE_URL

mysql = create_engine(MYSQL_DATABASE_URL, echo=True)  
postgres = create_engine(POSTGRES_DATABASE_URL, echo=True)

def create_databases():
  if not database_exists(mysql.url):
    create_database(mysql.url)

  if not database_exists(postgres.url):
    create_database(postgres.url)

def create_tables():
  meta = MetaData()
  contacts = Table(
    'contacts', meta, 
    Column('id', Integer, primary_key = True), 
    Column('nome', String(200)), 
    Column('celular', String(20)),
  )
  meta.create_all(mysql)
  meta.create_all(postgres)