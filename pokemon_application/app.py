from flask import Flask, render_template, request
from web_login_handler import pokemon_password_checker
from web_sign_up import create_new_trainer
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
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('sign_up.html')
    
    elif request.method == 'POST':
        submitted_id = request.form.get('trainer_id')
        submitted_email = request.form.get('email_id')
        raw_key = request.form.get('access_key')
        signup_status = create_new_trainer(submitted_id, submitted_email, raw_key)
        if signup_status == "SUCCESS":
            return render_template('index.html', message="Account created successfully!")
        elif signup_status == "TAKEN":
            return render_template('sign_up.html', error="Trainer ID already taken. Choose another one.")
if __name__ == '__main__':
    app.run(debug=True)