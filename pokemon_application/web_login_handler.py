#login to pokemon application and main body.
import hashlib
import sqlite3
def pokemon_password_checker(user_name,enter_password):
    connect = sqlite3.connect("pokemon_application/pokemon_master.db")
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM pokemon_table WHERE username =?",(user_name,))
    user_data = cursor.fetchone()
    if user_data==None:
        connect.close()
        return "NOT FOUND"
    
    database_failed_attempts = user_data[3]
    database_is_locked = user_data[4]
    if database_is_locked == 1:
        connect.close()
        return "LOCKED"
    entered_hash = hashlib.sha256(enter_password.encode()).hexdigest()
    if entered_hash == user_data[2]:
        cursor.execute("UPDATE pokemon_table SET failed_attempts = 0 WHERE username = ?", (user_name,))
        connect.commit()
        connect.close()
        return "SUCCESS"
    else:
        database_failed_attempts += 1
        cursor.execute("UPDATE pokemon_table SET failed_attempts = ? WHERE username = ?", (database_failed_attempts, user_name))
        connect.commit()
        if database_failed_attempts >= 3:
            cursor.execute("UPDATE pokemon_table SET is_locked = 1 WHERE username = ?", (user_name,))
            connect.commit()
            connect.close()
            return "LOCKED"
        else:
            connect.close()
            return "FAILED"