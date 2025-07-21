from src import app


@app.route('/usuarios')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM usuarios;")
    data = cur.fetchall()
    return render_template('index.html', usuarios=data)