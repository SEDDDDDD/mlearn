from bs4 import BeautifulSoup

# 분석하고 싶은 HTML
html = """
<html><body>
    <h1 id="title">스크레이핑이란?</h1>
    <p id="body2">웹페이지를 분석하는것</p>
    <p>원하는 부분을 추출하는 것</p>
    </body></html>
"""
# HTML 분석
soup = BeautifulSoup(html,'html.parser')

# find() 로 원하는 부분 추출

title = soup.find(id="title")


body2 = soup.find(id="body2")





# <body> 는 왜 안돼는지 none 으로나옴


print()
print("title = "+ title.string)
print()
print("body2 = "+ body2.string)


