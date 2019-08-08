from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__, template_folder='templates')    # Create a new instance of the Flask class called "app"

@app.route('/')
def index():
    return render_template("Dojo_Survey_Index.html")

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template('Dojo_Survey_Index.html/') 

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.