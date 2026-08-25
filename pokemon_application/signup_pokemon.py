import sqlite3
from password_application.professional_password_creator_ import professional_password_creator
from password_application.email_otp import security_email_id
def database_creation():
    connect_database = sqlite3.connect("pokemon_application/pokemon_master.db")
    cursor = connect_database.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pokemon_table( 
    username TEXT UNIQUE,
    email TEXT,
    password_hash TEXT,
    failed_attempts INTEGER DEFAULT 0,
    is_locked BOOLEAN DEFAULT 0,
    team_data TEXT default 'empty')
    """)
    connect_database.commit()
    connect_database.close()
def registration_page_pokemon():
    database_creation()
    connect = sqlite3.connect("pokemon_application/pokemon_master.db")
    cursor = connect.cursor()
    while True:
        print("SIGN UP ")
        user_name = input("Enter your username: ")
        cursor.execute("select * from pokemon_table where username = ?", (user_name,))
        existing_user = cursor.fetchone()
        if existing_user != None:
            print("Username already taken .try another")
            continue
        else:
            email = security_email_id()
            password = professional_password_creator()
            cursor.execute("Insert INTO pokemon_table (username,email,password_hash) VALUES (?,?,?)",(user_name,email,password))
            connect.commit()
            connect.close()
        return