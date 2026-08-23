#enter password and check
# this project's main role is to compare the enter password with the one saved in the database (saved_loginid_password) with respect to the entered username
# this project is used at the login page
# after various unsuccessful attempts it can block the account of the user
import sqlite3
import hashlib
def password_checker(username,saved_password_hashed):
    enter_password = (input("enter your password: "))
    hashed_password = hashlib.sha256(enter_password.encode()).hexdigest()
    attempt_left = 3
    while attempt_left > 0:
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
                print("press 4 to RESET PASSWORD")
                lock_application = sqlite3.connect("saved_loginid_password.db")
                cursor = lock_application.cursor()
                cursor.execute("UPDATE Users SET locked = 1 where username=?", (username,) )
                lock_application.commit()
                lock_application.close()
                return
            enter_password = input("enter your password: ")
# end
# testing of the function
if __name__ == "__main__":
    print("testing the code")
    test_password = "123"
    username = "hithere"
    password_checker(username,test_password)
    print("test successful")
# test ended