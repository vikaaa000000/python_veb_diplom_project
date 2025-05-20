from flask import Flask, render_template
from flask import request
from database import add_user

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        userame = request.form['username']
        email = request.form['email']
        password = request.form['password']
        print(f"Username: {userame}, Email: |{email}, Password: {password}")
        add_user(userame, email, password)
    return render_template('sign_up.html', title="Региисрация")

@app.route("/")
def gide():
    return render_template("gide.html")

app.run(debug=True)