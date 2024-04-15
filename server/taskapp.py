from flask import Flask
import flask
import json
from flask_cors import CORS
from pathlib import Path
import time
import re

# app = Flask(__name__)
# CORS(app)

# @app.route("/")
# def hello():
#     return "Hello, World!"

# @app.route('/users', methods=["GET"])
# def users():
#     path = Path(__file__).parent / "users.json"
#     print("users endpoint reached...")
#     with open(path, "r") as f:
#         data = json.load(f)

#     # Lägg till en ny användare
#     new_user = {"username": "user4", "pets": ["hamster"]}
#     data.append(new_user)

#     # Skriv data tillbaka till JSON-filen
#     try:
#         with open(path, "w") as f:
#             json.dump(data, f, indent=4)
#     except Exception as e:
#         print("Error writing to users.json:", e)
#         return "Error writing to users.json", 500

#     return flask.jsonify(data)

# if __name__ == "__main__":
#     app.run("localhost", 6969)

class TaskApp:
    def __init__(self):
        pass
    
    @classmethod
    def new_task(cls):
        """create new task

        Returns:
            TaskApp: new classobject
        """
        task = TaskApp()
        return task
    
    def set_timer(self, t: int) -> None:
        """Sets a timer

        Args:
            t (int): Time in seconds
        """
        while t:
            mins, secs = divmod(t, 60)
            timer = f'{mins}:{secs}'
            print(timer, "\n")
            time.sleep(1)
            t -= 1

    

class User:
    def __init__(self, name, password, mail):
        self._name = None
        self._password = None
        self._mail = None
        self.name = name
        self.password = password
        self.mail = mail

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        pattern = r"^[a-zA-ZåäöÅÄÖ]{3,20}+$"
        if not value:
            raise ValueError("Username cannot be empty")
        if not re.match(pattern, value):
            raise ValueError("Invalid username")
        self._name = value
    
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, value):

        pattern = r"^(?=.*[0-9])(?=.*[\W_]).{8,}$"
        if not value:
            raise ValueError("Password cannot be empty")
        if not re.match(pattern, value):
            raise ValueError("Password needs atleat 8 characters, including 1 digit and 1 special")
        self._password = value

    @property
    def mail(self):
        return self._mail

    @mail.setter
    def mail(self, value):
        pattern = r"^[a-z0-9_]+@[a-z]+\.(?:[a-z]{2,3}(?:\.[a-z]{2,3})?)+$"
        if not value:
            raise ValueError("Mail cannot be None")
        if not re.match(pattern, value):
            raise ValueError("Invalid email-adress")
        self._mail = value

if __name__ == "__main__":
    # task = TaskApp.new_task()
    # task.set_timer(100)
    try:
        user1 = User("Alice", "Pass1$asasd", "bajs@bajs.se")
        print("User1 created successfully!")
    except ValueError as e:
        print(e)  # Skriver ut eventuellt felmeddelande om validering misslyckades

    try:
        user2 = User("Bob", "123!asdasdasd", "test@se")
        print("User2 created successfully!")
    except ValueError as e:
        print(e)  # Skriver ut eventuellt felmeddelande om validering misslyckades