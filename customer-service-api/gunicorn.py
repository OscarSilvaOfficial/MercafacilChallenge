import multiprocessing
from api.utils.scripts import create_databases, create_tables

create_databases()
create_tables()

bind = '0.0.0.0:5000'

workers = multiprocessing.cpu_count() * 2 + 1

timeout = 120

loglevel = 'info'