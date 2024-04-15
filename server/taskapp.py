from flask import Flask
import flask
import json
from flask_cors import CORS
from pathlib import Path
import time

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route('/users', methods=["GET"])
def users():
    path = Path(__file__).parent / "users.json"
    print("users endpoint reached...")
    with open(path, "r") as f:
        data = json.load(f)

    # Lägg till en ny användare
    new_user = {"username": "user4", "pets": ["hamster"]}
    data.append(new_user)

    # Skriv data tillbaka till JSON-filen
    try:
        with open(path, "w") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print("Error writing to users.json:", e)
        return "Error writing to users.json", 500

    return flask.jsonify(data)

if __name__ == "__main__":
    app.run("localhost", 6969)

class TaskApp:
    def __init__(self):
        pass
    
    @classmethod
    def new_task(cls):
        task = TaskApp(cls)
        return task
    
    def set_timer(self, t: int):
        """Sets a timer

        Args:
            t (int): Time in seconds
        """
        while t:
            mins, secs = divmod(t, 60)
            timer = f'{mins}:{secs}'
            print(timer, "end\n")
            time.sleep(1)
            t -= 1

    


