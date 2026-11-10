import psycopg2

conn = psycopg2.connect(
    dbname="test_db",
    user="test_user",
    password="test_password",
    host="db_pq",
    port="5432"
)
print("Connected to PostgreSQL successfully")
conn.close()