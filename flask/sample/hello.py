from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    hello = "Hello, World!"
    return hello

if __name__ == "__main__":
    app.run()
    """
    こっちだと変更して保存すると自動で反映される
    エラー時にインタラクティブデバッガが使える
    """
    # app.run(debug=True)