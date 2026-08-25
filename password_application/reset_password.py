# reset_password.py project is the main page for resetting the password .
# reset password via otp . otp will be sent on email id provided by the user while creating password.
# has two uses. 1. to unblock user account after resetting password . 2. acts as forgot password window resets password.
# there are two functions in this project.1. send_real_email() and reset_password()
#in send_real_email(), the inbuilt function from email.message library is called and email id is provided through which email is sent for resetting purposes.
# it uses smptplib as a medium to send the email, to the user carrying the otp
#function is later used in reset_password() function as a building block .
# the other function reset_password() takes username if gone directly at reset password page .if gone after login page it fetches username through created_password_verifier
#this one created otp which is again automatically created by a builtin Python library called random.
# after taking the username it recognises the email id created at the registration page ,at the time of account creation and sends the otp at that email.
# the otp entered is also verified here and the blocked account status is then changed to unblock after verification.
# for that this project also accesses the database and necessary changes are done to the database.
import sqlite3
from professional_password_creator_ import professional_password_creator
import random
import smtplib
from email.message import EmailMessage
def send_real_email(receiver_email, otp_code):
    sender_email = "Youremail@gmail.com"
    sender_password = "Enter your password here"  # Replace with your actual email password or app password
    msg = EmailMessage()
    msg['Subject'] = 'Password Reset Security Alert'
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg.set_content(f"""
    Hello,

    A request was made to reset your password.
    Your 6-digit verification code is: {otp_code}

    If you did not request this, please ignore this email.

    Securely,
    Master Security Vault System
    """)
    try:
        print(f"\nsending OTP to {receiver_email}...")
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
            smtp_server.login(sender_email, sender_password)
            smtp_server.send_message(msg)
        print("[System] >>> Email successfully delivered! <<<")
        return True
    except Exception as e:
        print(f"\n>>> ERROR: Failed to send email. Details: {e}")
        return False
#end
def reset_password(target_user=None):
    print("please ensure that your security email id is active")
    if target_user == None :
        target_user = input("please enter username: ")
    else:
        print("username: "+ target_user+"")
    reset_password_in_database = sqlite3.connect("saved_loginid_password.db")
    cursor = reset_password_in_database.cursor()
    cursor.execute("SELECT email_id from Users where username=?",(target_user,))
    user_data = cursor.fetchone()
    if user_data == None :
        print("the user: "+target_user+"does not exist")
        reset_password_in_database.close()
        return
    else:
        target_email = user_data[0]
        create_otp = random.randint(100000,999999)
        email_delivered = send_real_email(target_email, create_otp)
        if email_delivered== True:
            attempt_left = 3
            while attempt_left > 0:
                user_input = input("enter your 6 digit verification code.")
                if user_input == str(create_otp):
                    print("otp verified! proceed to reset your password.")
                    new_password =professional_password_creator()
                    cursor.execute("update Users SET password=?, locked=0 WHERE username=?",(new_password, target_user))
                    reset_password_in_database.commit()
                    print("successfully created new password")
                    return
                else:
                    attempt_left = attempt_left - 1
                    print("incorrect otp .attempt left: "+str(attempt_left))
            if attempt_left ==0:
                print("reset password failed.please try again later")
        else:
            print("sorry. email could not be sent.please try again later")
        reset_password_in_database.close()