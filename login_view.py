import login_helpers

def welcome_screen(user_name: str, user_last_name: str) -> None:
    print(f"welcome {user_name} {user_last_name}")

def login_screen(user_data: list) -> list | None:
    isverified = False
    is_email_verified = False
    user_name = ""
    user_password = ""
    while not is_email_verified:
        print("we in the outer while loop\n\n")
        user_email = input("Email: ")
        is_password_verified = False
        while not is_password_verified:
            print("we in the inner while loop\n\n")
            user_password = input("password: ")
            for user, properties in enumerate(user_data):
                print(f"we in the {user} iteration of the for loop")
                print(f"{user} : {properties}")
                if login_helpers.valid_credentials(user_email, properties["email"]):
                    is_email_verified = True
                    if login_helpers.valid_credentials(user_password, properties["password"]):
                        is_password_verified = True

            if login_helpers.continue_login():
                if is_email_verified:
                    continue
                break

            else:
                return
        #       return
        #     elif login_helpers.valid_credentials(user_email, properties["email"]):
        #       print("first instance of continue_login prompt")
        #       if not login_helpers.continue_login():
        #         print(f"we are still in the inner but, just below the first instance of continue_login")
        #         continue
        #   if login_helpers.continue_login():
        #     print("second instance of continue_login prompt")
        #     return
        
    if user_email and user_password:
        return (user_name, user_password)
    return None