from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def hello():
    hello = "Hello, World!"
    return hello

# @app.route("/")
# def name():
#     name = request.args.get("name")
#     hello = f"Hello, {name}"
#     return hello

# @app.route("/")
# def name_age():
#     name = request.args.get("name")
#     text = f"<h1>Hello, {name}!</h1><br>"
#     age = request.args.get("age")
#     text += f"<h2>your age is {age}</h2>"
#     return text

if __name__ == "__main__":
    # app.run()
    """
    こっちだと変更して保存すると自動で反映される
    エラー時にインタラクティブデバッガが使える
    """
    app.run(debug=True)