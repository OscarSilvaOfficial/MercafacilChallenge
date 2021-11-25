
  
FROM python:3.9.5

ENV FLASK_APP=run.py
ENV DATABASE_URL=mysql+pymysql://admin:admin@mysql_local/admin

RUN pip install gunicorn --upgrade pip

ADD . /customer-service-api
WORKDIR /customer-service-api

COPY . /requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt 

CMD ["gunicorn", "--config=gunicorn.py", "run:app"]
