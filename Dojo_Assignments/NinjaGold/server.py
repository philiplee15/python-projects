from flask import Flask, render_template, request, redirect, session
import random
import datetime
app = Flask(__name__)
app.secret_key = "4wk5f0x"
app.gold = 0

# session['count'] = 1
def hitormiss():
	flip = random.randrange(0,2)
	if flip == 1:
		return True
	else:
		return False
def setdate():
	return str(datetime.datetime.now()).split('.')[0]

@app.route('/')
def index():
	if not 'list' in session:
		session['list'] = []
	return render_template('index.html')
@app.route('/find', methods=['POST'])
def count():
	print(request.form['building'])
	val = request.form['building']
	chance = hitormiss()
	if(val == 'farm'):
		rand = random.randrange(10,21)
		if chance:
			print("hit")
			session['gold']+=rand
		else:
			rand = 0
	elif(val == 'cave'):
		rand = random.randrange(5,11)
		if chance:
			print("hit")
			session['gold']+=rand
		else:
			rand = 0
	elif(val == 'house'):
		rand = random.randrange(2,6)
		if hitormiss():
			print("hit")
			session['gold']+=rand
		else:
			rand = 0
	elif(val == 'casino'):
		rand = random.randrange(0,51)
		if hitormiss():
			print("hit")
			session['gold']+=rand
		else:
			session['gold']-=rand
	elif(val == 'reset'):
		session['gold'] = 0
		del session['list']
		render_template('index.html')
		return redirect('/')
		#also restore activity
	if chance:
		session['earned'] = ["Earned {} from the {}! {}".format(rand, val, setdate()), 'green']
	elif not chance and val == 'casino':
		session['earned'] = ["Entered a {} and lost {} golds... Ouch! {}".format(val, rand, setdate()), 'red']
	else:
		session['earned'] = ["Earned {} from the {}! {}".format(rand, val, setdate()), 'red']
	session['list'].insert(0, session['earned'])
	print(session['list'])
	render_template('index.html')
	return redirect('/')

# @app.route('/users', methods=['POST'])
# def create_user():
# 	print("Got Post Info")
# 	name = request.form['name']
# 	email = request.form['email']
# 	return render_template('success.html')
#
# @app.route('/users/<username>')
# def show_user_prof(username):
# 	print(username)
# 	return render_template('user.html')

app.run(debug=True)
