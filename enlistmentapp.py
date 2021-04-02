import sqlite3 as sql
from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# change to name of your database; add path if necessary
db_name = 'testdb.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name

# this variable, db, will be used for all SQLAlchemy commands
db = SQLAlchemy(app)

@app.route('/')
def enlist():
    con = sql.connect("testdb.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from StudentInfo")
   
    studentIn = cur.fetchall(); 
    return render_template('EnlistmentPage.html', rows = studentIn)

@app.route('/enlistSections')
def enlistNew():
	con = sql.connect("testdb.db")
	con.row_factory = sql.Row

	cur = con.cursor()
	cur.execute("select * from CSCI199")

	rows = cur.fetchall();
	return render_template('EnlistmentSectionsPage.html', rows = rows)

if __name__ == '__main__':
    app.run(debug=True)