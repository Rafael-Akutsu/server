from flask import Flask, render_template
from flask_mysqldb import MySQL

from os import getenv
from dotenv import load_dotenv

from src import app


load_dotenv()

app.config['MYSQL_HOST'] = getenv("MYSQL_HOST")
app.config['MYSQL_USER'] = getenv("MYSQL_USER")
app.config['MYSQL_PASSWORD'] = getenv("MYSQL_PASSWORD")
app.config['MYSQL_DB'] = getenv("MYSQL_DB")

mysql = MySQL(app)
