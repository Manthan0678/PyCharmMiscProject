import sqlite3
from password_application.professional_password_creator_ import professional_password_creator
import random
import smtplib
from email.message import EmailMessage
def send_real_email_pokemon(receiver_email, otp_code):
    sender_email = "YOUR_EMAIL_HERE@gmail.com"
    sender_password = "YOUR_APP_PASSWORD_HERE"
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
    pokemon application
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
def reset_password_pokemon(target_user=None):
    print("please ensure that your security email id is active")
    if target_user == None :
        target_user = input("please enter username: ")
    else:
        print("username: "+ target_user+"")
    reset_password_in_database = sqlite3.connect("pokemon_master.db")
    cursor = reset_password_in_database.cursor()
    cursor.execute("SELECT email from pokemon_table where username=?",(target_user,))
    user_data = cursor.fetchone()
    if user_data == None :
        print("the user: "+target_user+"does not exist")
        reset_password_in_database.close()
        return
    else:
        target_email = user_data[0]
        create_otp = random.randint(100000,999999)
        email_delivered = send_real_email_pokemon(target_email, create_otp)
        if email_delivered== True:
            attempt_left = 3
            while attempt_left > 0:
                user_input = input("enter your 6 digit verification code.")
                if user_input == str(create_otp):
                    print("otp verified! proceed to reset your password.")
                    new_password =professional_password_creator()
                    cursor.execute("update pokemon_table SET password_hash=?, is_locked=0 , failed_attempts=0 WHERE username=?",(new_password, target_user))
                    reset_password_in_database.commit()
                    reset_password_in_database.close()
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