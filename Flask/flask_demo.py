import re
from flask import Flask
app = Flask(__name__)
@app.route("/")
def index():
    return "<h1> Hello Puppy </h1>"

@app.route("/info")
def info():
    return "Puppies are Cute"

#dynamic routing
@app.route("/<name>")
def dynamic(name):
    return f"You are in {name} page"

# @app.route("/user/<name>")
# def dynamic_prof(name):
#     return f"100th letter {name[100]} "

if __name__ == "__main__":
    app.run(debug=True)