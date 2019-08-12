from flask import Flask, render_template, request, redirect, session
import random, datetime
app = Flask(__name__)  
app.secret_key = 'wowey, keep it safe' # set a secret key for security purposes

@app.route('/')          
def index():
    if 'current_gold' not in session:
        session['current_gold'] = 0
    if 'activities' not in session:
        session['activities'] = []
    return render_template("index.html")

@app.route('/process_money', methods=["POST"])
def process():
    hidden_input = request.form['hidden']
    if hidden_input == 'farm':
        session['gold'] = random.randint(10, 20)
        session['current_gold'] = int(session['current_gold']) + session['gold']
        session['location'] = 'farm'
        session['timer'] = datetime.datetime.now()
        session['activities'].append(['positive', f"Earned {session['gold']} from the {session['location']} ({session['timer']})"])
    elif hidden_input == 'cave':
        session['gold'] = random.randint(5, 10)
        session['current_gold'] = int(session['current_gold']) + session['gold']
        session['location'] = hidden_input
        session['timer'] = datetime.datetime.now()
        session['activities'].append(['positive', f"Earned {session['gold']} from the {session['location']} ({session['timer']})"])
    elif hidden_input == 'house':
        session['gold'] = random.randint(2, 5)
        session['current_gold'] = int(session['current_gold']) + session['gold']
        session['location'] = hidden_input
        session['timer'] = datetime.datetime.now()
        session['activities'].append(['positive', f"Earned {session['gold']} from the {session['location']} ({session['timer']})"])
    elif hidden_input == 'casino':
        session['gold'] = random.randint(-50, 50)
        session['current_gold'] = int(session['current_gold']) + session['gold']
        session['location'] = hidden_input
        session['timer'] = datetime.datetime.now()
        if int(session['gold']) < 0:
            session['activities'].append(['negative', f"Lost {session['gold']} from the {session['location']} ({session['timer']})"])
        else:
            session['activities'].append(['positive', f"Earned {session['gold']} from the {session['location']} ({session['timer']})"])
    return redirect('/')

@app.route('/destroy_session')
def destroy():
        session.clear()
        return redirect('/')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template('index.html') 

if __name__=="__main__":   
    app.run(debug=True)    