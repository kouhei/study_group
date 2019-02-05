from flask import Flask, redirect ,request,render_template, url_for

app = Flask(__name__)

users = [{"id":"id", "pass":"pass"}]

@app.route("/", methods=["POST"])
def index():
    if request.method == "POST":
        uid = request.form["id"]
        pw = request.form["pass"]
        if {"id":uid, "pass":pw} in users:
            return render_template("index.html", id=uid)
        else:
            return "失敗<a href='/login'>log in</a>"

@app.route("/login", methods=["GET"])
def login():
    return render_template("login.html")

if __name__ == '__main__':
    app.run(debug=True)