from bs4 import BeautifulSoup

html = """
    <html><body>
        <div id="meigen">
            <h1>위키북스 도서</h1>
                <ul class="items">
                    <li>유니티 게임 이펙트 입문</li>
                    <li>스위프트로 시작하는 아이폰 앱 개발 교과서</li>
                    <li>모던 웹사이트 디자인의 정식</li>
                </ul>
            </div>
        </body>
    </html>
"""

# HTML 분석

soup = BeautifulSoup(html, 'html.parser')

# title 추출

title = soup.select_one("div#meigen > h1").string
li_list = soup.select("div#meigen > ul.items > li")

for li in li_list:
    print(f"li > {li.string}")
print(li_list)
