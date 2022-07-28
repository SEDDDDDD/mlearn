from bs4 import BeautifulSoup

# 분석하고 싶은 HTML
html = """
<html><body>
    <h1>스크레이핑이란?</h1>
    <p>웹페이지를 분석하는것</p>
    <p>원하는 부분을 추출하는 것</p>
    </body></html>
"""

# HTML 분석
soup = BeautifulSoup(html,'html.parser')

# 원하는 부분 추출
h = soup.html
h1 = soup.html.body.h1
p1 = h1.next_sibling.next_sibling
p2 = p1.next_sibling
p3 = p2.next_sibling.next_sibling


print(type(h))
print("h = "+ h1.string)        # h 태그의 문자열
print("h1 = "+ h1.string)       # h1 태그의 문자열
print("p1 = "+ p1.string)       # p1 태그의 문자열
print("p2 = "+ p2.string)       # p1 태그 이후 엔터 공백
