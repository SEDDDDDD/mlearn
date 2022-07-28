from bs4 import BeautifulSoup
import urllib.request as req

url = "https://finance.naver.com/marketindex/"

#url 데이터 가져오기
res = req.urlopen(url)

#beautifulsoup 으로 html 문자로 바꾸기
soup = BeautifulSoup(res,'html.parser')

# 원하는 요소의 문자열을 보기위해 select 함수를 이용
#oilGoldList > li.on > a.head.gasoline > div > span.value
price = soup.select_one("#oilGoldList > li.on > a.head.gasoline > div > span.value").string


# 뭐이따구야
print("usd/krw =", price)

