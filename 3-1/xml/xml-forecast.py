from bs4 import BeautifulSoup
import urllib.request as req
import os.path


url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
savename = "forecast.xml"
if not os.path.exists(savename):
    req.urlretrieve(url, savename)

xml = open(savename, "r", encoding="utf-8").read()
soup = BeautifulSoup(xml, 'html.parser')


print(soup)
# info={} # 딕셔너리 생성
# for location in soup.find_all("location"):
#     # soup에서(html 문자열) location 태그 의 내용을 location 변수에 넣음
#     name = location.find('city').string
#     # location 변수에 들어간 내용중 city 태그의 내용을 문자열로 name에 저장
#     weather = location.find('wf').string
#     # loctaion 변수에 들어간 내용중 wf 태그의 내용을 문자열로 weather 에 저장
#     if not (weather in info):
#         # info 딕셔너리에 weather 변수 내용이 없다면
#         info[weather] = []
#         # 데이터 형식이 리스트를 weather 키값에 할당
#         # 여기서 print(info) 를 입력하면 info = { 흐림:[], 흐리고비:[] } 이렇게 작성되있음
#     info[weather].append(name)
#     # weather 키값은 리스트이므로 그 리스트 안에 append 함수로 name 값을 할당
#     # 그럼 info = {흐림 : [1, 2, 3,...], 흐리고비:[4, 5, 6, 7 ,... ]}이런 식으로 작성 되있음
#                 #  키  :   키값             키  :     키값
# for weather in info.keys():
#     # info 의 키를 weather 변수에 넣음
#     print("+", weather)
#     for name in info[weather]:
#         # info 의 키값을 name 변수에 넣음
#         print("| - ",name)
#
# print(info["흐림"])
# print(type(soup))



