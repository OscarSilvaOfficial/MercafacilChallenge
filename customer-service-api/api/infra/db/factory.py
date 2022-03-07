from api.infra.db.mysql_drive import MySql
from api.infra.db.postgres_drive import Postgres

def mysql_factory() -> MySql:
  return MySql('localhost', '3306', 'admin', 'admin', 'admin', 'contacts')

def postgres_factory() -> Postgres:
  return Postgres('localhost', '5432', 'admin', 'admin', 'postgres', 'contacts')
