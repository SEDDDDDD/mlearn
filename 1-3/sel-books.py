from bs4 import BeautifulSoup
fp = open("books.html", encoding="utf-8")
soup = BeautifulSoup(fp, 'html.parser')

sel = lambda q: print(soup.select_one(q).string)

sel("#nu")
sel("li:nth-of-type(4)")
sel("ul>li#nu")
sel("#bible > #nu")
sel("ul#bible > li#nu")
sel("li[id='nu']")
sel("#bible #nu")
sel("li#nu")

# 그외의 방법
print(soup.select("li")[3].string)
print(soup.find_all("li")[3].string)