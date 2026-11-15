import pymysql

conn = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="school123",
    database="task_manager"
)
cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM users")
print(cursor.fetchone())
conn.close()