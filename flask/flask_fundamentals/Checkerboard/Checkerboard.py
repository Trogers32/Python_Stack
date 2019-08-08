from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__, template_folder='templates')    # Create a new instance of the Flask class called "app"

@app.route('/')
def play1():
    return render_template("index.html", width=8, height=8)

@app.route('/<x>')
def play2(x):
    x = int(x)
    return render_template("index.html", width=8, height=x)

@app.route('/<x>/<y>')
def play3(x,y):
    x = int(x)
    y = int(y)
    return render_template("index.html", width=x, height=y)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template('index.html/') 

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.