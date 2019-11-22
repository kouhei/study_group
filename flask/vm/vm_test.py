import json
drink = json.load("ファイル名")

x = {"name":"cola\t","price":150,"number":20,"temp": "cool"}
y = {"name":"山田コーヒー","price":10,"number":100,"temp": "hot"}
z = {"name":"Seven Stars","price":500,"number":50,"temp": "cool"}
drink=[x,y,z]

for num, i in enumerate(drink):
    if i["number"] > 0:
        print(str(num) + "\t" + i["name"] + "\t" + str(i["price"]) + "\t" + i["temp"] + "\t" + "販売中")
    else:
        print(str(num) + "\t" + i["name"] + "\t" + str(i["price"]) + "\t" + i["temp"] + "\t" + "売り切れ")

num = int(input("番号を入力してください"))
print(str(drink[num]["price"]) + "円です")

money = int(input("お金を入れてください"))

while True:
    if money < drink[num]["price"]:
        m = drink[num]["price"] - money
        print(str(m) + "円足りません")
        ne = int(input("不足金を投入してください"))
        money += ne
    elif money == drink[num]["price"]:
        print(drink[num]["name"] + "が出ました。")
        break
    else:
        n = money - drink[num]["price"]
        print(drink[num]["name"] + "が出ました。" + "\n" + "おつりは" + str(n) + "円です")
        break

drink[num][number] -= 1