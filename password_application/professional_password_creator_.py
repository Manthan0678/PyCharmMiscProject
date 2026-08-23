# creating a password with a special character, a capital letter , minimum 8 characters and a number
#professional_password_creator_.py project file asks for input and only creates password.
# this file is used in many places of the application .
#1 . registration page (for creating password)
#2. reset password and forgot password page (again to make new password)
import hashlib
def professional_password_creator():
    print("""Create a strong password 
     kindly follow the instructions"
    1. password should have at least one special character
    2. password should have at least one uppercase letter
    3. password should have at least one number
    4. password should have at least 8 character""")

    capital_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    special_character = "!@#$%^&()"
    while True:
        create_password = input("create your password: ")
        has_upper = False
        has_special_character = False
        has_number = False
        if len(create_password) < 8:
            print("password should have at least 8 character")
            continue
        for letters in create_password:
            if letters in capital_letters:
                has_upper = True
            elif letters in numbers:
                has_number = True
            elif letters in special_character:
                has_special_character = True
        if has_upper==True and has_number==True and has_special_character==True:
            while True:
                print("please reenter the password to confirm  ")
                confirm = input("confirm your password  ")
                if confirm == create_password :
                   print("password created successfully")
                   encoded_password =create_password.encode()
                   hashed_password = hashlib.sha256(encoded_password).hexdigest()
                   return hashed_password
                else:
                     print("password do not match")
        elif has_upper==True and has_number==True and has_special_character==False:
            print("password has missing special character")
        elif has_upper==True and has_number==False and has_special_character==True:
            print("password has missing number")
        elif has_upper==False and has_number==True and has_special_character==True:
            print("password has missing capital letter")
        elif has_upper == False and has_number == False and has_special_character == True:
            print("password has missing capital letter and number")
        elif has_upper == False and has_number == True and has_special_character == False:
            print("password has missing capital letter and special character ")
        elif has_upper == True and has_number == False and has_special_character == False:
            print("password has missing number and special character ")
        elif has_upper == False and has_number == False and has_special_character == False:
            print("password has missing number , special character and capital letter")
# testing of the function.
if __name__ == "__main__":
    professional_password_creator()