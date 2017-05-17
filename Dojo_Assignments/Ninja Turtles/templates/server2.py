from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "4wk5f0xx"

@app.route('/')
def index():
    if 'random' not in session:
        session['random'] = randrange(0,101)
	return render_template('randomnumgame.html')
@app.route('/result', method="post")
def result():
    print(request.form)
    num = session['random']
    guess = request.form['']
    if 'submit' in request.form:
