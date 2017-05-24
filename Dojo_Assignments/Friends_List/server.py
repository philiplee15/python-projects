from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'friendsdb')

@app.route('/')
def index():
    friends = mysql.query_db("SELECT * FROM friends")
    print(friends)
    return render_template('index.html', all_friends=friends)
@app.route('/friends', methods=['POST'])
def create():
	fname = request.form['first_name']
	lname = request.form['last_name']
	age = request.form['age']
	if not isinstance(age, (int, float, complex)):
		print('hello')
	query = "INSERT INTO friends (first_name, last_name, age, created_at, updated_at) VALUES (:first_name, :last_name, :age, NOW(), NOW())"
	data = {
			'first_name': fname,
			'last_name': lname,
			'age': age
			}
	print(data)
	mysql.query_db(query, data)
	return redirect('/')
app.run(debug=True)
