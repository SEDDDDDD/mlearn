from bs4 import BeautifulSoup


html = """
    <html><body>
        <ul>
            <li><a href="http://naver.com">naver.com</a></li>
            <li><a href="http://daum.net">daum.net</a></li>
        </ul>
    </body>
    </html>
"""
#html 분석
soup = BeautifulSoup(html,'html.parser')

#find_all()메서드로 추출

links = soup.find_all("a")

#링크 출력

for a in links:
    print(a.attrs)
    href = a.attrs["href"]  # 해당 속성 값을 딕셔너리 "{키:값}" 형태로 출력
    STR = a.string
    print(f"URL > {href}")
    print(f"문자열 > {STR}")
