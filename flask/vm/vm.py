import os
import json

class VendingMachine():
    if os.path.dirname(__file__):
        json_path = os.path.dirname(__file__)+"/items.json"
    else:
        json_path = "./items.json"

    def __init__(self, items_list):
        self.money = 0
        #items_listが与えられなければjsonで読み込んだやつ使う
        items = []
        if os.path.exists(VendingMachine.json_path):
            with open(VendingMachine.json_path) as f:
                items = json.load(f, encoding="utf-8")
        self.ITEMS_LIST = items
        if items_list:
            # print("itemlist!!!!!!!:",items_list)
            self.ITEMS_LIST += items_list

    def input_money(self, money):
        if money >= 0:
            self.money += money
        else:
            return -1

    def get_items(self):
        return self.ITEMS_LIST

    def show_items(self):
        output = ""
        for i, item in enumerate(self.ITEMS_LIST):
            str = f"{i} item: {item['name']} price: {item['price']} "
            if item["stock"] == 0:
                str += "売切"
            else:
                str += "販売中"
            output += str+"\n"
        print(output)

    def select_item(self, selected_id):
        if self.ITEMS_LIST[selected_id]["stock"] <= 0:
            return -1
        if selected_id is -1:
            return -1
        return self.ITEMS_LIST[selected_id]

    def get_money(self):
        return self.money

    def calc_charge(self, item):
        return self.get_money() - item["price"]

    def pay(self,price):
        self.money -= price

    def buy(self, item):
        charge = self.calc_charge(item)
        if charge >= 0:
            self.pay(item["price"])
            item["stock"] -= 1
            return {"can_buy":True, "money":self.get_money()}
        else:
            return {"can_buy": False, "money": charge*-1}


    def main_buy(self,item):
        charge = self.calc_charge(item)
        if charge >= 0:
            print(f"{item['name']}が買えました")
            self.pay(item["price"])
            item["stock"] -= 1
            print(f"残金: {self.get_money()}")
            return self.get_money()
        else:
            print(f"{charge*-1}円足りません")
            return -1

    def add_item(self, new_item):
        for item in self.ITEMS_LIST:
            if new_item["name"] == item["name"]:
                print("おなじやつあるぞ")
                return -1
        self.ITEMS_LIST.append(new_item)

    def save_items_list(self):
        with open(VendingMachine.json_path, "w") as f:
            json.dump(self.ITEMS_LIST, f, ensure_ascii=False)

def input2int(message=""):
        return int(input(message))

if __name__ == "__main__":
    vm = VendingMachine([])
    # items_list = [{"name":"緑茶", "price":120, "stock":20},{"name":"オレンジジュース", "price":150, "stock":10}]
    # for item in items_list:
    #     vm.add_item(item)

    vm.show_items()
    while True:
        coin = vm.input_money(input2int("お金を入れて: "))
        if coin is -1:
            break
    while True:
        item = vm.select_item(input2int("商品を選択して: "))
        if item == -1:
            print('購入終了')
            break
        money = vm.main_buy(item)
        if money <= 0:
            break
    print(str(vm.get_money())+"円のおつりです")
    vm.save_items_list()