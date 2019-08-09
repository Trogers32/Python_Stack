from flask import Flask, render_template, request, redirect, session  # Import Flask to allow us to create our app
app = Flask(__name__, template_folder='templates')    # Create a new instance of the Flask class called "app"
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

@app.route('/')
def index():
    return render_template("Dojo_Survey_Index.html")

@app.route('/result', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    session['name_from_form'] = request.form['name']
    session['location_from_form'] = request.form['locations']
    session['language_from_form'] = request.form['languages']
    session['comment_from_form'] = request.form['comment']
    return redirect('/show')

@app.route('/show')
def show_user():
    return render_template("result.html", name_on_template=session['name_from_form'], 
        location_on_template=session['location_from_form'], language_on_template=session['language_from_form'], comment_on_template=session['comment_from_form'])



@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template('Dojo_Survey_Index.html/') 

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.