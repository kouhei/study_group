"""
https://qiita.com/ikaro1192/items/11717d5ce4c46868c967
次のようにディクショナリでIDとパスワードが与えられる
    http://127.0.0.1:5000/login?id=hoge&pass=foo
    のようなURLに対してアクセスが来た際、
    ログインに成功すれば /success
    失敗すれば /failに飛ばすようにせよ"""
from flask import Flask, redirect, url_for, request
app = Flask(__name__)
users_data = [{"id":"yamada","pass":"taro"},{"id":"id", "pass":"pass"}, {"id":"admin","pass":"0000"}]

@app.route("/")
def index():
    return "hello"

@app.route("/login")
def login():
    uid = request.args.get("id")
    pw = request.args.get("pass")
    if {"id":uid, "pass":pw} in users_data:
        return redirect(url_for("success"))
    return redirect(url_for("fail"))

@app.route("/success")
def success():
    return "success!"

@app.route("/fail")
def fail():
    return "fail..."


if __name__ == "__main__":
    app.run(debug=True)