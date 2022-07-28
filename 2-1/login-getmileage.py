import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


# 아이디 ,비밀 번호 지정
# m_id
# m_password
# http://www.myhanbit.co.kr/myhanbit/myhanbit.html
m_id = "dudgh3"
m_passwd = "dudgh8864!"



# 세션 시작
session = requests.session()

# 로그인 실행
login_info = {
    "m_id" : m_id,
    "m_passwd" : m_passwd
}


# 로그인 수행
url_login = "https://www.hanbit.co.kr/member/login_proc.php"
res = session.post(url_login, data=login_info)
res.raise_for_status()

# 마이페이지 접근
url = "https://www.hanbit.co.kr/myhanbit/myhanbit.html"
res = session.get(url)

res.raise_for_status()



# 마일리지 , 이코인 가져오기
soup = BeautifulSoup(res.text, 'html.parser')

mileage = soup.select_one("#container > div > div.sm_mymileage > dl.mileage_section1 span").text
ecoin = soup.select_one("#container > div > div.sm_mymileage > dl.mileage_section2 span").text


print(f"마일리지 : {mileage}")
print(f"이코인 : {ecoin}")




