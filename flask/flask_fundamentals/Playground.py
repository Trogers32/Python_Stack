from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__, template_folder='templates')    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return render_template('index.html', phrase='hello', times=5)  # Return the string 'Hello World!' as a response

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<name>')
def say(name):
    try:
        int(name)
        return "Sorry! No response. Try again."
    except ValueError:
        return "Hi " + name + "!"

@app.route('/repeat/<num>/<content>')
def repeater(num, content):
    try:
        num = int(num)
        try:
            int(content)
            return "Sorry! No response. Try again."
        except ValueError:
            return (f"{content}\n" * num)
    except TypeError:
        return "Sorry! No response. Try again."
    except ValueError:
        return "Sorry! No response. Try again."

@app.route('/play')
def play1():
    return render_template("index.html", times=3)

@app.route('/play/<x>')
def play2(x):
    x=int(x)
    return render_template("index.html", times=x, other_color="rgb(50, 143, 160)")

@app.route('/play/<x>/<color>')
def play3(x, color):
    x=int(x)
    return render_template("index.html", times=x, other_color=color)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template('index.html/') 

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.