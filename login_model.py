
from pathlib import Path
import json
from typing import Dict, Optional

_USERS_PATH = Path(__file__).parent / "data.json"

def load_users() -> list[Dict]:

    with open(_USERS_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
        return data

def find_user_by_email(email: str, users: list[Dict]) -> Optional[Dict]:
    """Return the user dict matching email or None if not found."""
    email_lower = email.strip().lower()
    for user in users:
        if user.get("email", "").strip().lower() == email_lower:
            return user
    return None

def verify_password(user: Dict, password: str) -> bool:
    """Verify password for a user record. Replace with hashed check if needed."""
    return user.get("password", "") == password
