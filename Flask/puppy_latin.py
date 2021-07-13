from flask import Flask
import flask

app = Flask(__name__)

@app.route("/")
def index():
    return f"<h1> Go To /puppy_latin/name/</h1>"

@app.route("/puppy_latin/<puppy>")
def puppy_latin(puppy):
    if puppy.lower()[-1] == 's':
        lp = puppy[:-1] + 'y'
    elif puppy.lower()[-1] == 'y':
        lp = puppy + 'iful'
    else:
        lp = puppy

    return f"Hello {lp}"

if __name__ == '__main__':
    app.run(debug=True)