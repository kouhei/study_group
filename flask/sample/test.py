from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def calc():
    op = request.args.get("op")
    a = int(request.args.get("a"))
    # print(a, type(a))
    # a = int(a)
    b = int(request.args.get("b"))
    # print(b, type(b))
    if op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    else:
        result = f"対応していない演算子です op:{op}"
    return str(result)

if __name__ == "__main__":
    # app.run()
    """
    こっちだと変更して保存すると自動で反映される
    エラー時にインタラクティブデバッガが使える
    """
    app.run(debug=True)