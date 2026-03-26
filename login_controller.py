import login_model
import login_view
import login_helpers

def main_loop() -> None:
    users = login_model.load_users()

    while True:
        email = login_view.prompt_email()
        user = login_model.find_user_by_email(email, users)
        password = login_view.prompt_password()
        if user:
            # Email exists: prompt for password until success or user quits
            while True:
                #password = login_view.prompt_password()
                if login_model.verify_password(user, password):
                    login_view.show_welcome(user["first_name"], user["last_name"])
                    return
                # wrong password for an existing email
                if login_helpers.prompt_continue("Incorrect password. Try again? (y/n) "):
                    continue
                else:
                    login_view.show_goodbye()
                    return
        else:
            # Email not found: ask whether to retry email+password
            if login_helpers.prompt_continue("Email not found. Try again? (y/n) "):
                continue
            else:
                login_view.show_goodbye()
                return

if __name__ == "__main__":
    main_loop()
