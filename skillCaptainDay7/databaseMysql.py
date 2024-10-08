import mysql.connector

def connect_query():
    connection = mysql.connector.connect(
        host='localhost',
        database='enable_v2_db',
        user='root',
        password='root'
    )

    cursor = connection.cursor()
    query = "SELECT * FROM backend_lanes"
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)


connect_query()
