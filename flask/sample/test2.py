from flask import Flask, request, redirect, url_for
app = Flask(__name__)

#URLを変数に
@app.route("/user/<username>")
def show_user(username):
    return f"User: {username}"

#リダイレクト
# @app.route("/")
# def index():
#     return redirect("/login")

# @app.route("/login")
# def login():
#     return "login"


#関数名からURLに(#文字列で渡した関数名のURLを返す)
#urlでなく、関数名と動きを関連づけられるので、URLを変えるのが簡単
@app.route("/")
def index():
    return "hello"

@app.route("/not_found")
def not_found():
    return redirect(url_for("index"))

if __name__ == "__main__":
    # app.run()
    """
    こっちだと変更して保存すると自動で反映される
    エラー時にインタラクティブデバッガが使える
    """
    app.run(debug=True)