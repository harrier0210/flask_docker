import mysql.connector
import time

#DBコンテナ起動まで待機
for i in range(60):
    try:
        connector = mysql.connector.connect(
                    user='root',
                    password='test',
                    host='maria_db',
                    database='test')
        break
    except Exception as e:
        print('Waiting for DB setting completion...')
        time.sleep(1)
