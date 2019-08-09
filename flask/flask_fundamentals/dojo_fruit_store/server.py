from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')          
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    fname = request.form['first_name']
    lname = request.form['last_name']
    full_name = fname + " " + lname
    strawberries = request.form['strawberry']
    raspberries = request.form['raspberry']
    apples = request.form['apple']
    stid = request.form['student_id']
    amount = int(strawberries) + int(raspberries) + int(apples)
    return render_template("checkout.html", fname=fname, lname=lname, full_name=full_name, strawberries=strawberries, raspberries=raspberries, apples=apples, stid=stid, amount=amount)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    