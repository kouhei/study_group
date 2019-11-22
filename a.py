import json
with open("./flask/vm/items.json") as f:
    drinks = json.load(f)

print(drinks[0])
drinks[0]["stock"] -= 1
print(drinks[0])

with open("./flask/vm/items.json", "w") as f:
    json.dump(drinks, f)