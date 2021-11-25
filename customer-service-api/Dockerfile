
  
FROM python:3.9.5

ENV FLASK_APP=run.py
ENV AUTH_SERVICE_API=http://customer_auth_service_api:5001
ENV MYSQL_DATABASE_URL=mysql+pymysql://admin:admin@mysql_local/admin?charset=utf8mb4
ENV POSTGRES_DATABASE_URL=postgresql+psycopg2://admin:admin@postgresql_local/postgres

RUN pip install gunicorn --upgrade pip

ADD . /customer-service-api
WORKDIR /customer-service-api

COPY . /requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["gunicorn", "--config=gunicorn.py", "run:app"]
