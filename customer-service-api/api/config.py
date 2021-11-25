import os

SECRET=os.getenv('SECRET', 'ashdfashdfuioahdeusifhjiaudhgvq390713984ryfuhif')
MYSQL_DATABASE_URL=os.getenv('MYSQL_DATABASE_URL', 'mysql+pymysql://admin:admin@localhost:3306/admin?charset=utf8mb4')
POSTGRES_DATABASE_URL=os.getenv('POSTGRES_DATABASE_URL', 'postgresql+psycopg2://admin:admin@localhost/postgres')
AUTH_SERVICE_API=os.getenv('AUTH_SERVICE_API', 'http://localhost:5001')