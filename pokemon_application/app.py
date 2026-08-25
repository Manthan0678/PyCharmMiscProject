from flask import Flask, render_template, request
import sqlite3
import hashlib

from streamlit import status

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/login', methods=['POST'])
def login():
    submitted_id = request.form.get('trainer_id')
    raw_key = request.form.get('access_key')

    encoded_key = raw_key.encode()
    hashed_key = hashlib.sha256(encoded_key).hexdigest()

    conn = sqlite3.connect('pokemon_application/pokemon_master.db')    
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pokemon_table WHERE username=?", (submitted_id,))
    trainer = cursor.fetchone()

    if trainer!= None:
        from login_password_pokemon import pokemon_password_checker
        conn.close()
        stored_hashed_key = trainer[2]
        failed_attempts = trainer[3]
        is_locked = trainer[4]
        from web_login_handler import pokemon_password_checker
        status = pokemon_password_checker(submitted_id, stored_hashed_key, hashed_key)
        if status == True:
            return render_template('dashboard.html', trainer_id=submitted_id)
        else:
            return render_template('index.html', error="Invalid Password.")
    else:
        conn.close()
        return render_template('index.html', error="Invalid Trainer ID or Access Key.")

if __name__ == '__main__':
    app.run(debug=True)