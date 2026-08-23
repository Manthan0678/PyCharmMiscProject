# created_password_verifier.py serves as the main login page .
# it asks for login id , connects to the database and checks about its presence.
# after taking and confirming the login id it runs the function password_checker() imported from password project.
#this project returns the login id to the main application . this one is used various times  inside the application, so user does not have to enter the login id again and again.
#end
from password import password_checker
import sqlite3
def created_password_verifier():
    print("welcome")
    enter_login_id =  input("enter your login id: ")
    connect_server = sqlite3.connect("saved_loginid_password.db")
    cursor = connect_server.cursor()
    cursor.execute("SELECT password, locked FROM Users WHERE username = ?", (enter_login_id,) )
    data_base_output = cursor.fetchone()
    if data_base_output == None:
        print("login id not found")
        connect_server.close()
        return None
    else:
        saved_password = data_base_output[0]
        locked_status = data_base_output[1]
        if locked_status == 1:
            print("ALERT! This account is currently locked.")
            print("press 4 from main menu to reset password via otp")
            connect_server.close()
            return enter_login_id
        else:
            password_checker(enter_login_id , saved_password)
            connect_server.close()
            return enter_login_id
if __name__ == "__main__":
    created_password_verifier()