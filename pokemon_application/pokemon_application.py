# main pokemon application
print("welcome to pokemon application")
def pokemon_application():
    print("""
    PRESS 1 TO GET STATS AND INFORMATION ON POKEMON
    PRESS 2 TO SIGN UP
    PRESS 3 TO SIGN IN 
    PRESS 4 TO RESET PASSWORD 
    PRESS 5 TO EXIT
    """)
    user_input = input("Enter your choice: ")
    if user_input == "1":
        from get_pokemon_data import fetch_pokemon_data
        print("Welcome to the Global Pokedex Terminal")
        while True:
            target = input("\nEnter a pokemon name to scan (or type 'exit' to quit): ").strip()
            if target.lower() == 'exit':
                pokemon_application()
            elif target == "":
                print("you did not enter anything .")
                continue
            else:
                fetch_pokemon_data(target)
    elif user_input == "2":
        from login_password_pokemon import login_pokemon
        from signup_pokemon import registration_page_pokemon
        registration_page_pokemon()
        user_input2 = input("PRESS 1 TO SIGN IN . PRESS ANY OTHER KEY TO EXIT ")
        if user_input2 == "1":
            login_pokemon()
        else:
            return
    elif user_input == "3":
        from login_password_pokemon import login_pokemon
        login_pokemon()
    elif user_input == "4":
        from pokemon_password_recovery import reset_password_pokemon
        reset_password_pokemon(target_user=None)
    elif user_input == "5":
        return
    else:
        print("invalid input")
        pokemon_application()
if __name__=="__main__":
    pokemon_application()