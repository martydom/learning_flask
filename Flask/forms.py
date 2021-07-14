from flask import Flask,render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route('/signup')
def signup():
    return render_template("signup.html")

@app.route("/thankyou")
def thankyou():
    fn = request.args.get('first')
    ln = request.args.get('last')
    return render_template('thankyou.html', first=fn,last=ln)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True)