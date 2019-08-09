import random
from flask import Flask, render_template, request, redirect, session  # Import Flask to allow us to create our app
app = Flask(__name__, template_folder='templates')    # Create a new instance of the Flask class called "app"
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

@app.route('/')
def index():
        if 'number' not in session:
                session['number'] = round(random.randint(1,100))
        return render_template("Number_Game_Index.html")

@app.route('/destroy_session')
def destroy():
        session.clear() #or v
        # session.pop('counter', None)
        return redirect('/')

@app.route('/guess', methods=["POST"])
def set_counter():
        session['guess'] = request.form['guess']
        return render_template("result.html", prev_guess=int(session['guess']))

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template('Number_Game_Index.html/') 

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.