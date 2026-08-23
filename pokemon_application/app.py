from flask import Flask, render_template, request

app = Flask(__name__)

# This is your default route that loads the UI
@app.route('/')
def home():
    return render_template('index.html')

# This is the NEW route that handles the login logic
@app.route('/login', methods=['POST'])
@app.route('/login', methods=['POST'])
@app.route('/login', methods=['POST'])
def login():
    submitted_id = request.form.get('trainer_id')
    submitted_key = request.form.get('access_key')

    if submitted_id == "RED_001" and submitted_key == "pikachu123":
        # THE NEW CONNECTION: Load the dashboard and pass the ID directly into the HTML!
        return render_template('dashboard.html', trainer_id=submitted_id)
    else:
        # We will make the error screen pretty later, let's just get the success path working
        return "<h1>ACCESS DENIED: Invalid Trainer ID or Access Key.</h1>"
if __name__ == '__main__':
    app.run(debug=True)