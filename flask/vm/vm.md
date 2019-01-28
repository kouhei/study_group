# 自販機flaskで
## ラフ
- /で自販機の購入画面
- /adminで管理者モードに(パスワードつけてもOK)

##items.JSON仕様
```json
[
    {
        "name": "商品名",
        "price": 価格(int),
        "stock": 在庫数(int)(optional)
    }
]
```

## flaskの流れ
1. 表示(商品リスト表示)

## POST
### 種類
- 買う
- 
### POSTのjson仕様
```{
    "params":{} or []
}```

## 注意点
- JSでjsonでPOSTするときは```Content-Type: application/json```がいるっぽい