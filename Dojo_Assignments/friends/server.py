from flask import Flask, request, redirect, render_template, session, flash
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'friendsdb')
# an example of running a query
@app.route('/')
def index():
    friends = mysql.query_db("SELECT * FROM friends")
    print(friends)
    return render_template('index.html')
@app.route('/friends', methods=['POST'])
def create():
    return redirect('/')
app.run(debug=True)
