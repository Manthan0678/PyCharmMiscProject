from flask import Flask, render_template, request
from web_login_handler import pokemon_password_checker

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/login', methods=['POST'])
def login():
    submitted_id = request.form.get('trainer_id')
    raw_key = request.form.get('access_key')

    login_status = pokemon_password_checker(submitted_id, raw_key)
    if login_status == "SUCCESS":
        return render_template('dashboard.html', trainer_id=submitted_id)
    elif login_status == "LOCKED":
        return render_template('index.html', error="ACCOUNT LOCKED. Please reset your password.")
    elif login_status == "FAILED":
        return render_template('index.html', error="Invalid password.")
    elif login_status == "NOT FOUND":
        return render_template('index.html', error="Trainer ID not found.")


if __name__ == '__main__':
    app.run(debug=True)