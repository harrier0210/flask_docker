import mysql.connector
import time

#DBコンテナ起動まで待機
for i in range(60):
    try:
        connector = mysql.connector.connect(
                    user='python',
                    password='python',
                    host='maria_db',
                    database='sample')
        break
    except Exception as e:
        print('Waiting for DB setting completion...')
        time.sleep(1)
