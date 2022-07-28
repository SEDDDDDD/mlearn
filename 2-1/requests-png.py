import requests

r = requests.get("https://t1.daumcdn.net/cfile/tistory/99DD2E335D44C66915")

with open("test.png", "wb") as f:
    f.write(r.content)

print("saved")