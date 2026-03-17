import login_view
import login_model
import login_helpers

def main_loop():
  user_data = login_model.get_user_data()
  verified_user = login_view.login_screen(user_data)
  if verified_user:
    login_view.welcome_screen(verified_user[0], verified_user[1])
  else:
    print("goodbye...")
  return 

main_loop()