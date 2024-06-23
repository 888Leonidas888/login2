from flask import Flask
from flask import render_template, redirect, url_for
from flask import request
from storage import Storage

app = Flask(__name__)


@app.route("/")
def login():
    return render_template('login.html')

@app.route("/validate", methods=['POST'])
def validate():
    data = request.get_json()
    email = data['email']
    password = data['password']

    cnn = Storage()
    cnn.connect()
    result = cnn.validate_user(email, password)
    if result:
        return redirect(url_for('welcome', email=email))
    return render_template('login.html')

@app.route("/welcome/<email>")
def welcome(email):
    return render_template('welcome.html', email=email)


if __name__ == '__main__':
    app.run(debug=True)
