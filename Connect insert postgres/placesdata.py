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
create table if not exists data(
    id int,
    user_id int,
    place_code varchar(255),
    address varchar(255),
    postcode int,
    district varchar(255),
    sub_district varchar(255),
    thana varchar(255),
    type varchar(255),
    sub_type varchar(255),
    longitude float,
    latitude float
);
'''
cur.execute(createTable)
with open("places_202408131151.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    insertTable = "INSERT INTO data (id, user_id, place_code, address, postcode, district, sub_district, thana, type, sub_type, longitude, latitude) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    for row in reader:
        cur.execute(insertTable, (int(row[0]), int(row[1]), str(row[2]) , str(row[3]) , str(row[4]) , str(row[5]) , str(row[6]) , str(row[7]) , str(row[8]) , str(row[9]) , float(row[10]), float(row[11])))
conn.commit()
cur.close()
print("Inserted Successfully!")