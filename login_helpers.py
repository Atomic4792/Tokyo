def valid_credentials(field, condition) -> bool:
  #validation logic here
  return field == condition
  
def continue_login() -> bool:
  answer = ""
  while not answer:
    choice = input("invalid email or password, would you like to try again? (y/n)").lower()
    if choice not in ("yes", "y", "no", "n"):
      print("Please enter a valid choice")
      continue
    answer = choice
  if answer in ("y", "yes"):
    return True
  return False