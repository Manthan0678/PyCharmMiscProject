# taking note of the security email id from user at the registration page to reset password .
# the main purpose of this project is to only accept the email is of the user.
def security_email_id():
    print("please enter your email id.")
    print("email id is required if you want to reset your password via otp")
    print("email id should be only of GMAIL(google mail)")
    email_suffix = "@gmail.com"
    while True:
        security_email_id = input("please enter your email id : ")
        if security_email_id.endswith(email_suffix):
            print("email accepted")
            while True:
                confirm_email_id = input("please reenter email id to confirm : ")
                if confirm_email_id == security_email_id:
                    print("security email id stored in database")
                    return security_email_id
                else:
                    print("email does not match. Try again.")
        else:
            print("enter valid email id")
if __name__ == "__main__":
    security_email_id()