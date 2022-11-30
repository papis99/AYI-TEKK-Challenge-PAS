import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="demo_python"
)

with mysql.connector.connect(
host="localhost",
    user="root",
    password="12345678",
    database="demo_python"
) as db :
    with db.cursor() as c:
        c.execute("insert into test (txt) \
                   values ('david')")
        db.commit()