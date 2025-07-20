from flask import Flask, render_template
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'senha123'
app.config['MYSQL_DB'] = 'flask_db'

mysql = MySQL(app)

@app.route('/usuarios')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM usuarios;")
    data = cur.fetchall()
    return render_template('index.html', usuarios=data)


if __name__ == '__main__':
    app.run(debug = True)