import urllib.request
import urllib.parse

API = "https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

# 매개변수 인코딩
values = {
   'stnId':'184'
}
params = urllib.parse.urlencode(values)
print(params)
# 요청 전용 url 생성

url = API + "?" + params
print("url=", url)

# 다운로드
data = urllib.request.urlopen(url).read()
text = data.decode("utf-8")
print(text)

