from flask import Flask, render_template, request
import sqlite3
import hashlib

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
    cursor.execute("SELECT * FROM pokemon_table WHERE username=? AND password_hash=?", (submitted_id, hashed_key))
    trainer = cursor.fetchone()
    conn.close()

    if trainer:
        return render_template('dashboard.html', trainer_id=submitted_id)
    else:
        return render_template('index.html', error="Invalid Trainer ID or Access Key.")
if __name__ == '__main__':
    app.run(debug=True)