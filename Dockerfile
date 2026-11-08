FROM python:3.9

WORKDIR /app

RUN pip install pytest psycopg2-binary

COPY . /app

CMD ["python", "db_ckecker.py"]