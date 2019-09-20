import mysql.connector

class DB:

    connector = mysql.connector.connect(
                user='root',
                password='test',
                host='maria_db',
                database='test')
    cursor = connector.cursor(dictionary=True)

    def execute(sql, data=None):
        DB.cursor.execute(sql, data)
        DB.close()
        return DB.cursor.fetchone()

    def execute_list(sql, data=None):
        DB.cursor.execute(sql, data)
        DB.close()
        return DB.cursor.fetchall()

    def update(sql, data=None):
        DB.cursor.execute(sql, data)
        DB.connector.commit()
        DB.close()

    def close():
        DB.cursor.close
        DB.connector.close
