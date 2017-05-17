from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def form():
	return render_template('form.html')

@app.route('/process', methods=['POST'])
def process():
	language = request.form['language']
	location = request.form['location']
	name = request.form['name']
	comment = request.form['comment']
	print(language, location, name, comment)
	return render_template('success.html', language = language, location = location, name = name, comment = comment )
	#return redirect('/')

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
