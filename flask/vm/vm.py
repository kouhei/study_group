import os
import json

class VendingMachine():
    json_path = "./items.json"
    def __init__(self,ITEMS_LIST):
        self.money = 0
        #ITEMS_LISTが与えられなければjsonで読み込んだやつ使う
        items = []
        if os.path.exists(VendingMachine.json_path):
            with open(VendingMachine.json_path) as f:
                items = json.load(f, encoding="utf-8")
        self.ITEMS_LIST = items
        if ITEMS_LIST:
            self.ITEMS_LIST = ITEMS_LIST

    def input_money(self):
        money = int(input("お金を入れて: "))
        if money >= 0:
            self.money += money
        else:
            return -1

    def get_items(self):
        return self.ITEMS_LIST

    def show_items(self):
        for i, item in enumerate(self.ITEMS_LIST):
            str = f"{i} item: {item['name']} price: {item['price']} "
            if item["stock"] == 0:
                print(str+"売切")
            else:
                print(str+"販売中")

    def select_item(self):
        selected_id = int(input("商品を選択して: "))
        if selected_id is -1:
            return -1
        return self.ITEMS_LIST[selected_id]

    def get_money(self):
        return self.money

    def calc_charge(self, item):
        return self.get_money() - item["price"]

    def pay(self,price):
        self.money -= price

    def buy(self,item):
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
        self.ITEMS_LIST.append(new_item)

    def save_items_list(self):
        with open(VendingMachine.json_path, "w") as f:
            json.dump(self.ITEMS_LIST, f, ensure_ascii=False)

if __name__ == "__main__":
    vm = VendingMachine(ITEMS_LIST=[])
    # items_list = [{"name":"緑茶", "price":120, "stock":20},{"name":"オレンジジュース", "price":150, "stock":10}]
    # for item in items_list:
    #     vm.add_item(item)

    vm.show_items()
    while True:
        coin = vm.input_money()
        if coin is -1:
            break
    while True:
        item = vm.select_item()
        if item == -1:
            print('購入終了')
            break
        money = vm.buy(item)
        if money <= 0:
            break
    print(str(vm.get_money())+"円のおつりです")
    vm.save_items_list()