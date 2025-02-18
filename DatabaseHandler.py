import json

from User import User


class DatabaseHandler:
    def __init__(self, filename="user_data.json"):
        self.filename = filename

    def save_user(self, user):
        data = {
            "name": user.name,
            "history": [(q.text, correct) for q, correct in user.history]
        }
        with open(self.filename, "w") as f:
            json.dump(data, f)

    def load_user(self, name):
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                user = User(name)
                user.history = data.get("history", [])
                return user
        except FileNotFoundError:
            return User(name)