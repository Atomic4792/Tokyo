import login_helpers

def welcome_screen(user_name: str, user_last_name: str) -> None:
    print(f"welcome {user_name} {user_last_name}")

def login_screen(user_data: list) -> bool:
  isverified = False
  while not isverified:
    print("we in the outer while loop\n\n")
    user_email = input("Email: ")
    while True:
      print("we in the inner while loop\n\n")
      user_password = input("password: ")
      for user, properties in enumerate(user_data):
        print(f"we in the {user} iteration of the for loop")
        print(f"{user} : {properties}")
        if login_helpers.valid_credentials(user_email, properties["email"]) and login_helpers.valid_credentials(user_password, properties["password"]):
          isverified = True
          return
        elif login_helpers.valid_credentials(user_email, properties["email"]):
          print("first instance of end_login prompt")
          if not login_helpers.end_login():
            print(f"we are still in the inner but, just below the first instance of end_login")
            continue
      if login_helpers.end_login():
        print("second instance of end_login prompt")
        r
    
  return isverified