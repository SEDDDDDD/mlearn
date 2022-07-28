import json
price = {
    "date": "2017-05-10",
    "price": {
        "Apple": 80,
        "Orange": 55,
        "Banana": 40
    }
}
print(price)
print()
s = json.dumps(price, indent=4)
print(s)