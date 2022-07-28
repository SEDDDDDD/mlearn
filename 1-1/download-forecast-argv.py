import sys
import urllib.request as req
import urllib.parse as parse

API = "https://n.news.naver.com/mnews/article/215/0001041271"

if len(sys.argv) <= 1:
   print("USAGE: download-forecast-argv.py <newsNumber>")
   sys.exit()

newsNumber = sys.argv[1]

print(len(sys.argv))
# print(sys.argv[0])
# print(sys.argv[1])


# 매개변수 인코딩
values = {
   'sid': newsNumber
}
params = parse.urlencode(values)
print(params)

# 요청 전용 url 생성
url = API + "?" + params
print("sid=", url)

# 다운로드
data = req.urlopen(url).read()
text = data.decode("utf-8")
print(text)


