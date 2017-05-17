from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def default():
	return render_template("index.html")

@app.route('/ninja')
def ninja():
	return render_template("directory.html", src='Ninjas/tmnt.png')
	#return redirect('/')
@app.route('/ninja/<ninja>')
def color(ninja):
	if ninja == 'orange':
		print(ninja)
		n = 'Ninjas/michelangelo.jpg'
		print(n)
	elif ninja == 'red':
		n = 'Ninjas/raphael.jpg'
	elif ninja == 'blue':
		print(color)
		n = 'Ninjas/leonardo.jpg'
	elif ninja == 'purple':
		n = 'Ninjas/donatello.jpg'
	else:
		n = 'Ninjas/notapril.jpg'


	return render_template("ninja.html", color=color, src=n)


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
