import csv
import psycopg2
conn = psycopg2.connect(
    database="demodb",
    user="postgres",
    password="bkoi2017",
    host="localhost",
    port="5432"
)
cur = conn.cursor()
createTable = '''
create table if not exists users(
    id int,
    name varchar(255),
    email varchar(255)
);
'''
cur.execute(createTable)
with open("users_202408131733.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    insertTable = "INSERT INTO users (id, name, email) VALUES (%s, %s, %s)"
    for row in reader:
        cur.execute(insertTable, (int(row[0]), str(row[1]), str(row[2])))
conn.commit()
cur.close()
print("Inserted Successfully!")