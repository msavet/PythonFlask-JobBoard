import sqlite3
from flask import g
from flask import Flask, render_template

PATH = 'db/jobs.sqlite'


app = Flask(__name__)
def open_connection():
    connection = getattr(g, '_connection', None)
    if connection == 'None':
        connection = g._connection = sqlite3.connect(PATH)
    row_factory.connection = sqlite3.Row
    return connection

def execute_sql():
    connection = open_connection()
    sql = ""
    values = ()
    commit = False
    single = False
    cursor = exec(connection, sql + values)
    if commit == True:
        results = connection.commit()
    else:
        results = (cursor.fetchone(), single, cursor.fetchall())
        cursor.close
        return results
@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')