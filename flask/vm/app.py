from flask import Flask, render_template, request
from vm import VendingMachine
app = Flask(__name__)

vm = VendingMachine([])
@app.route("/")
def init():
    money = request.args.get("money")
    money = int(money) if money else 0
    items = vm.get_items()
    html = render_template('index.html', items=items, money=money)
    return html

@app.route("/select_item")
def select_item():
    money = int(request.args.get("money"))
    vm.input_money(money)
    money = vm.get_money()
    items = vm.get_items()
    return render_template("select_item.html", money=money, items=items)

@app.route("/buy")
def buy():
    selected_item_id = int(request.args.get("selected_item_id"))
    items = vm.get_items()
    item = items[selected_item_id]
    dic = vm.buy(item)
    if dic["can_buy"]:
        message = f"{item['name']}が買えました！"
        vm.save_items_list()
        money = dic["money"]
        return render_template("select_item.html", message=message, money=money, items=items)

    message = f"{dic['money']}円足りません"
    money = vm.get_money()
    return render_template("select_item.html", message=message, money=money, items=items)


if __name__ == "__main__":
    app.run(debug=True)