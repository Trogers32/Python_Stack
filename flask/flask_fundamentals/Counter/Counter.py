from flask import Flask, render_template, request, redirect, session  # Import Flask to allow us to create our app
app = Flask(__name__, template_folder='templates')    # Create a new instance of the Flask class called "app"
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

@app.route('/')
def index():
        if 'main_counter' in session:
                session['main_counter'] = session['main_counter'] + 1
        else:
                session['main_counter'] = 1
        if 'counter' in session:
                if 'user_c' in session:
                        if 'temp' in session:
                                session['counter'] = int(session['counter'])+int(session['user_c'])
                                session['user_c'] = session['temp']
                        else:
                                session['counter'] = int(session['counter'])+int(session['user_c'])
                                session['user_c'] = 1
                else:
                        session['user_c'] = 1
        else:
                session['counter'] = 1
        return render_template("Counter_Index.html", count = session['counter'], main_counter = session['main_counter'])

@app.route('/destroy_session')
def destroy():
        session.clear() #or v
        # session.pop('counter', None)
        return redirect('/')

@app.route('/destroy_counter')
def destroy_counter():
        session.pop('counter', None)
        return redirect('/')

@app.route('/add_two')
def addtwo():
        session['user_c'] = 2
        return redirect('/')

@app.route('/set_counter', methods=["POST"])
def set_counter():
        session['temp'] = request.form['user_counter']
        session['user_c'] = request.form['user_counter']
        return redirect('/')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template('Counter_Index.html/') 

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.