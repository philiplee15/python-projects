from flask import Flask, render_template, request, redirect, session, flash
import random
app = Flask(__name__)
app.secret_key = "4wk5f0xx"

def setnum():
    session['random'] = random.randint(1,100)

@app.route('/')
def index():
    if 'random' not in session:
        setnum()
    else:
        pass
    return render_template('randomnumgame.html')

@app.route('/result', methods=["POST"])
def result():
    num = session['random']
    guess = request.form['val']
    if 'submit' in request.form:
        if not guess.isdigit():
            print("ok")
            session['some'] = "Must input integer value."
            session['class'] = 'wrong'
            flash('Correct', 'success')
        elif num > int(guess):
            session['some'] = "Too low, you go."
            session['class'] = 'low'
        elif num < int(guess):
            session['some'] = "Too high, you fly."
            session['class'] = 'high'
        else:
            session['some'] = "Winner, winner chicken dinner."
            session['class'] = 'win'
    render_template('randomnumgame.html')
    print(request, session, num, guess)
    return redirect('/')
@app.route('/reset', methods=["POST"])
def reset():
    print(request.form)
    if 'reset' in request.form:
        print('hi')
        session.clear()
        session['some'] = ""
        session['class'] = ''
    render_template('randomnumgame.html')
    return redirect('/')


app.run(debug=True)
