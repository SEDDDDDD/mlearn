import requests
import time
import os

a = 1
def clear():
    os.system('cls')
while a == 1:
    r = requests.get("http://api.aoikujira.com/time/get.php")

    print(r.text)

    print(r.content)

    clear()
    time.sleep(1)