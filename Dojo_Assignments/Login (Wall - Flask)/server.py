'''
bugs to fix:
#password hash matching - @login - SHA256, @SQL - SHA2(input, 256)
#posts - show posts username not session username
#remove feature - associate proper post id to post render to access that later
#user session resetting too often and how to route back to root without having to logout
'''

from flask import Flask, flash, redirect, render_template, request, session, abort
from mysqlconnection import MySQLConnector
import re
import os
import hashlib
import binascii

app = Flask(__name__)
app.secret_key = '4wk5f0x'
mysql = MySQLConnector(app, 'friendsdb')

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('form.html')
    else:
        selectQ = """SELECT users.id, CONCAT(users.first_name, ' ', users.last_name) as 'full', users.username, users.created_at, posts.id as 'POSTID', posts.text
        FROM users
        LEFT JOIN posts
        ON users.id = posts.user_id
        ORDER BY posts.id DESC
        """
        commentPostQ = """SELECT users.id, CONCAT(users.first_name, ' ', users.last_name) as 'full', users.username, posts.id as 'postid', posts.created_at, comments.id as 'cid', comments.comment, comments.created_at, comments.post_id as 'cpid', comments.user_id as 'cuid'
        FROM users
        LEFT JOIN posts
        ON users.id = posts.user_id
        RIGHT JOIN comments
        ON comments.user_id = users.id
        """
        userposts = mysql.query_db(selectQ)
        usercomments = mysql.query_db(commentPostQ)
        return render_template('wall.html', userposts = userposts, usercomments = usercomments)

@app.route('/login', methods=['POST'])
def do_admin_login():
    user = request.form['username']
    inputpw = request.form['password']
    passwordQ = "SELECT users.password FROM users WHERE users.username = \'" +user+"\'"
    userQ = "SELECT users.id FROM users WHERE users.username = \'" +user+"\'"
    if mysql.query_db(userQ):
        userpw = mysql.query_db(passwordQ)[0]['password']
        userid = mysql.query_db(userQ)[0]['id']
        if hashlib.sha256(inputpw.encode('utf-8')).hexdigest():            
            session['logged_in'] = True
            session['user'] = userid
        else:
            session['logged_in'] = False
            flash('PW or login incorrect.')
    else:
        flash('Login or PW incorrect.')
    return redirect('/')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/wallpost', methods=['POST'])
def postcomment():
    comment = request.form['wallpost']
    if comment:
        insertQ = "INSERT INTO posts (text, user_id, created_at, updated_at) VALUES (\'"+comment+"\',"+str(session['user'])+", NOW(), NOW())"
        mysql.query_db(insertQ)
    else:
        pass
    return home()
@app.route('/comment', methods=['POST'])
def comment():
    comment1 = request.form['text']
    userid = request.form['userid']
    postid = request.form['postid']
    print(comment1)
    commentQ = """INSERT INTO comments (comment, created_at, updated_at, post_id, user_id)
    VALUES (:comment1, NOW(), NOW(), :postid, :userid)
    """
    data = {
        "comment1": comment1,
        "postid": postid,
        "userid": userid
    }
    if comment1:
        mysql.query_db(commentQ, data)
    else:
        pass
    return home()
@app.route('/delete', methods=['POST'])
def delete():
    test = request.form['postid']
    removeQ = "DELETE FROM posts WHERE posts.id ={}".format(test)
    mysql.query_db(removeQ)
    return redirect('/')

@app.route('/success', methods=['POST'])
def success():
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    PW_REGEX = re.compile(r'[a-zA-Z0-9]{8,20}')
    fname = request.form['fname']
    lname = request.form['lname']
    email = request.form['email']
    username = request.form['username']
    password = request.form['password']
    confirm = request.form['confirm']
    validated = True
    if len(fname) < 2 or len(lname) < 2:
        flash('Your name field(s) are too short.')
        validated = False
    if not EMAIL_REGEX.match(email) or len(email) < 1:
        flash('Your e-mail is invalid.')
        validated = False
    if not PW_REGEX.match(password):
        flash('Your password is invalid.')
        validated = False
    if password != confirm:
        flash('Passwords do not match.')
        validated = False
    if validated == True:
        query = "INSERT INTO users (first_name, last_name, username, password, email, created_at, updated_at) VALUES (:fname, :lname, :uname, :pname, :ename, NOW(), NOW())"
        data = {
            "fname": fname,
            "lname": lname,
            "uname": username,
            "pname": hashlib.sha256(request.form['password'].encode('utf-8')).hexdigest(),
            "ename": email
            }
        mysql.query_db(query, data)
        flash('Registration successful, you may login to continue.')
        return redirect('/')
    return render_template('register.html')

@app.route('/logout')
def logout():
    session['logged_in'] = False
    return home()
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=5000)
