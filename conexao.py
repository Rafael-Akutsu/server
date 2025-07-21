from flask import Flask, render_template
from flask_mysqldb import MySQL

from os import getenv
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)

app.config['MYSQL_HOST'] = getenv("MYSQL_HOST")
app.config['MYSQL_USER'] = getenv("MYSQL_USER")
app.config['MYSQL_PASSWORD'] = getenv("MYSQL_PASSWORD")
app.config['MYSQL_DB'] = getenv("MYSQL_DB")

mysql = MySQL(app)

@app.route('/usuarios')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM usuarios;")
    data = cur.fetchall()
    return render_template('index.html', usuarios=data)


if __name__ == '__main__':
    app.run(debug = True)