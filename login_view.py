import login_helpers

def welcome_screen(user_name: str, user_last_name: str) -> None:
    print(f"welcome {user_name} {user_last_name}")

def login_screen(user_data: list) -> list | None:
    is_email_verified = False
    user_email = ""
    user_password = ""
    while not is_email_verified:
        print("we in the outer while loop\n\n")
        user_email = input("Email: ")
        is_password_verified = False
        while not is_password_verified:
            print("we in the inner while loop\n\n")
            user_password = input("password: ")
            idk_what_to_call_this_flag = False
            found_user_password = ""
            if not idk_what_to_call_this_flag:
            #add conditional here for when user is already found and we want to query against it again
                for user, properties in enumerate(user_data):
                    print(f"we in the {user} iteration of the for loop")
                    print(f"{user} : {properties}")
                    if login_helpers.valid_credentials(user_email, properties["email"]):
                        is_email_verified = True
                        found_user_password = properties["password"]
                        user_email = properties["email"]
                        if login_helpers.valid_credentials(user_password, properties["password"]):
                            is_password_verified = True
                            user_password = properties["password"]
                            break
                        elif login_helpers.continue_login():
                            idk_what_to_call_this_flag = True
                            break
                        else:
                            return None 
                if not is_email_verified:
                    if login_helpers.continue_login():
                        break
                    return None
                else:
                    continue


                # if login_helpers.continue_login():
                #     idk_what_to_call_this_flag = True
                #     break
                # return None

            else:
                if login_helpers.valid_credentials(user_password, found_user_password):
                    is_password_verified = True
                    is_email_verified = True
                else:
                    return None

            # if login_helpers.continue_login():
            #     if is_email_verified:
            #         continue
            #     break

            # else:
            #     return
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
        return (user_email, user_password)
    return None