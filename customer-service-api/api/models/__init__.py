from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from api.config import MYSQL_DATABASE_URL, POSTGRES_DATABASE_URL

mysql = create_engine(MYSQL_DATABASE_URL)
postgres = create_engine(POSTGRES_DATABASE_URL)

db_mysql = sessionmaker(autocommit=False, autoflush=False, bind=mysql)
db_postgres = sessionmaker(autocommit=False, autoflush=False, bind=postgres)

db = {
  'mysql': db_mysql(),
  'postgres': db_postgres()
}

Base = declarative_base()
