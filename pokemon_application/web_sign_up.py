import hashlib
import sqlite3
import re  

def create_new_trainer(username, email, raw_password):
    password_pattern = r"^(?=.*\d)(?=.*[A-Z])(?=.*[!@#$%^&*()]).{8,}$"
    
    if not re.match(password_pattern, raw_password):
        return "WEAK_PASSWORD"

    hashed_password = hashlib.sha256(raw_password.encode()).hexdigest()
    
    connect = sqlite3.connect("pokemon_application/pokemon_master.db")
    cursor = connect.cursor()
    
    try:
        cursor.execute("INSERT INTO pokemon_table (username, email, password_hash) VALUES (?, ?, ?)", 
                       (username, email, hashed_password))
        connect.commit()
        connect.close()
        return "SUCCESS"
        
    except sqlite3.IntegrityError:
        connect.close()
        return "TAKEN"