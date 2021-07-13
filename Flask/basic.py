from os import name
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/child/<name>")
def inher(name):
    return render_template("inherit.html",name=name)


@app.route('/new')
def new_page():
    name = "Deva"
    letters = list(name) 
    return render_template("new1.html",name = name,letters=letters)


@app.route("/control")
def control():
    mylist  = list(range(11))
    return render_template('control.html',mylist=mylist)



if __name__ == "__main__":
    app.run(debug=True)