
def prompt_email() -> str:
    return input("Email: ").strip()

def prompt_password() -> str:
    return input("Password: ").strip()

def show_welcome(first_name: str, last_name: str) -> None:
    print(f"\nWelcome {first_name} {last_name}\n")

def show_message(msg: str) -> None:
    print(msg)

def show_goodbye() -> None:
    print("Goodbye...")