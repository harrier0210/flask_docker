from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

connector = mysql.connector.connect(
            user='python',
            password='python',
            host='maria_db',
            database='sample')

cursor = connector.cursor()

@app.route("/")
def hello():

    html = "<h3>Hello {name}!</h3>"
    return html.format(name=os.getenv("NAME"))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
