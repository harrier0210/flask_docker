import mysql.connector

class DB(object):

    def __init__(self):
        self.connector = ""
        self.cursor = ""

    def connect(self):
        self.connector = mysql.connector.connect(
                    user='root',
                    password='test',
                    host='maria_db',
                    database='test')
        self.cursor = self.connector.cursor(dictionary=True)

    def execute(self, sql, data=None):
        self.cursor.execute(sql, data)
        self.close()
        return self.cursor.fetchone()

    def execute_list(self, sql, data=None):
        self.cursor.execute(sql, data)
        self.close()
        return self.cursor.fetchall()

    def update(self, sql, data=None):
        self.cursor.execute(sql, data)
        self.close()

    def commit(self):
        self.connector.commit()

    def close(self):
        self.cursor.close
        self.connector.close
