def valid_credentials(field: str, condition: str) -> bool:
    return field == condition

def prompt_continue(message: str = "Would you like to try again? (y/n) ") -> bool:
    while True:
        choice = input(message).strip().lower()
        if choice in ("y", "yes"):
            return True
        if choice in ("n", "no"):
            return False
        print("Please enter 'y' or 'n'.")
