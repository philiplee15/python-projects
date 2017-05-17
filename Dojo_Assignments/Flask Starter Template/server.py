from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "4wk5f0x"
# session['count'] = 1

@app.route('/')
def index():
	return render_template('index.html')
@app.route('/count', methods=['POST', 'GET'])
def count():
	print(request.form)
	if 'count' not in session:
		session['count'] = 0
	if 'reset' in request.form:
		session['count'] = 0
		render_template('index.html')
		return redirect('/')
	if 'count' in request.form:
		# update = session['count']
		session['count']+=2
		render_template('index.html')
		return redirect('/')
@app.route('/users', methods=['POST', 'GET'])
def create_user():
	print("Got Form Info")
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
