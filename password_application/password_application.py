# Main password application.
# this is the main application which uses other projects as the building blocks
# the projects namely :professional_password_creator , password , password_creation_and_verification , created_password_verifier , email_otp , reset_password are used
# the data is stored in the database: saved_loginid_password.db
#this application takes input from the user about the required pathway and acts like a junction to the other programs including registration(account creation )
# login , resetting password.

#end
from password_creation_and_verification import password_creation_and_verification
from created_password_verifier import created_password_verifier
from reset_password import reset_password
print("Welcome to password application")
def password_application(remember_user=None):
    print("""
    PRESS 1 TO REGISTER 
    PRESS 2 TO LOGIN
    PRESS 3 TO EXIT
    PRESS 4 TO RESET PASSWORD
    """)
    pathway = (input("enter the pathway: "))
    if pathway == "1":
        password_creation_and_verification()
        user_input = input("PRESS 1 TO LOGIN PAGE, 2 TO RESET PASSWORD , 3 TO MAIN PAGE , 4 TO EXIT")
        if user_input == "1":
            login = created_password_verifier()
            password_application(login)
        elif user_input == "2":
            reset_password(remember_user)
            password_application()
        elif user_input == "3":
            password_application()
        elif user_input == "4":
            print("thankyou visit again. ")
        else:
            print("invalid input! please enter 1 or 2 or 3 or 4 . ")

    elif pathway == "2":
        user_login = created_password_verifier()
        password_application(user_login)
    elif pathway == "3":
        print("thank you visit again")
    elif pathway == "4":
        reset_password(remember_user)
        password_application()
    else:
        print("invalid input! please enter 1 or 2 or 3 or 4 . ")
if __name__ == "__main__":
    password_application()