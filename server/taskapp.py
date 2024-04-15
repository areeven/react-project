from flask import Flask
import flask
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route('/users', methods=["GET"])
def users():
    print("users endpoint reached...")
    with open("users.json", "r") as f:
        data = json.load(f)

    # Lägg till en ny användare
    new_user = {"username": "user4", "pets": ["hamster"]}
    data.append(new_user)

    # Skriv data tillbaka till JSON-filen
    try:
        with open("users.json", "w") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print("Error writing to users.json:", e)
        return "Error writing to users.json", 500

    return flask.jsonify(data)

if __name__ == "__main__":
    app.run("localhost", 6969)
