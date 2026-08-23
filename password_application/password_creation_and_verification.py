# password_creation_and_verification.py the main registration page of the application
#this project is the one where database(saved_loginid_password) is created .
#from professional_password_creator_ project  professional_password_creator() function is imported. it creates password
# from email_otp project security_email_id() function is imported. this function collects email id which is used while resetting password.
#end
from professional_password_creator_ import professional_password_creator
from email_otp import security_email_id
import sqlite3
def password_creation_and_verification():
    print("""
REGISTRATION PAGE
enter your username and create password to sign in
give your email id for resetting password (if needed)
    """)
    new_user = input("enter a username: ")
    save_password = sqlite3.connect("saved_loginid_password.db")
    executer = save_password.cursor()
    executer.execute("""
                     CREATE TABLE IF NOT EXISTS Users
                     (
                         username TEXT UNIQUE,
                         password TEXT,
                         locked INTEGER DEFAULT 0
                     )
                     """)
    try:
        executer.execute("ALTER table Users ADD COLUMN email_id TEXT")
        save_password.commit()
    except sqlite3.OperationalError:
        pass
    executer.execute("select * from Users where username = ?",(new_user,))
    existing_user = executer.fetchone()
    if existing_user != None:
        print("the username: "+new_user+ " is already taken! please try another.")
        save_password.close()
        return

    project_1 = professional_password_creator()
    project2 = security_email_id()
    new_mail = project2
    new_pass = project_1
    executer.execute("INSERT INTO Users (username, password, email_id) VALUES (?, ? , ?)", (new_user, new_pass, new_mail))
    save_password.commit()
    print("\n>>> SUCCESS: Account created! <<<")
    save_password.close()
    print("password saved in database")
    return new_user

if __name__ == "__main__":
    password_creation_and_verification()