#login to pokemon application and main body.
import hashlib
import sqlite3
from get_pokemon_data import fetch_pokemon_data
from creating_pokemon_team import build_pokemon_team
from pokemon_password_recovery import reset_password_pokemon
def pokemon_password_checker(username,saved_password_hashed,enter_password):
    attempt_left = 3
    while attempt_left > 0:
        hashed_password = hashlib.sha256(enter_password.encode()).hexdigest()
        if hashed_password == saved_password_hashed:
            print("correct password accepted")
            return True
        else:
            attempt_left = attempt_left - 1
            print("wrong password remaining attempt left : " + str(attempt_left))
            print("if you forgot password you can reset it from the main menu press 4")
            if attempt_left == 0:
                print("no more attempts access denied.")
                print("ACCOUNT IS NOW BLOCKED .")
                lock_application = sqlite3.connect("pokemon_application/pokemon_master.db")
                cursor = lock_application.cursor()
                cursor.execute("UPDATE pokemon_table SET is_locked = 1 where username=?", (username,) )
                lock_application.commit()
                lock_application.close()
                return False
def login_pokemon():
    print("LOGIN PAGE")
    user_name = input("enter your username: ")
    connect = sqlite3.connect("pokemon_application/pokemon_master.db")
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM pokemon_table WHERE username =?",(user_name,))
    user_data = cursor.fetchone()
    if user_data==None:
        print("trainer name: "+str(user_name)+" not found")
        connect.close()
        return None
    else:
        database_username = user_data[0]
        database_email = user_data[1]
        database_password = user_data[2]
        database_failed_attempts = user_data[3]
        database_is_locked = user_data[4]
        if database_is_locked == 1:
            print("trainer name: "+str(database_username)+" is locked due to 3 failed password attempts.")
            print("enter reset to change password . press any other key to exit")
            user_input = input("enter your choice: ").strip()
            if user_input == "reset":
                print("redirecting to password recovery page")
                reset_password_pokemon(user_name)
            else:
                return
        else:
            print("data found")
            password_passed = pokemon_password_checker(database_username,database_password)
            if password_passed == True:
                print("welcome trainer")
                while True:
                    print("""
                    Press 1 to go to pokedex
                    Press 2 to create pokemon team 
                    press 3 to reset password
                    press 4 to sign out.
                    """)
                    user_input = input("enter your choice: ")
                    if user_input == "1":
                        print("Welcome to the Global Pokedex Terminal")
                        while True:
                            target = input("\nEnter a pokemon name to scan (or type 'exit' to quit): ")
                            if target.lower() == 'exit':
                                break
                            elif target == "":
                                print("you did not enter anything!")
                                continue
                            else:
                                fetch_pokemon_data(target)
                    elif user_input == "2":
                        team = build_pokemon_team()
                        connect_database = sqlite3.connect("pokemon_application/pokemon_master.db")
                        cursor = connect_database.cursor()
                        cursor.execute("UPDATE pokemon_table SET team_data = ? where username = ?",(team, database_username))
                        connect_database.commit()
                        connect_database.close()
                    elif user_input == "3":
                        reset_password_pokemon(user_name)
                    elif user_input == "4":
                        return
                    else:
                        print("invalid input.")
            else:
                print("account locked due 3 incorrect password attempts")
                print("""
                Press 1 to reset password or press any other key to exit    
                """)
                pathway = input("enter choice: ")
                if pathway=="1":
                    print("redirecting to password recovery page")
                    reset_password_pokemon(user_name)
                else:
                    return