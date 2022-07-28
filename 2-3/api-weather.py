# api key       4068d6f78e8aed97f6610b6f072ddb22


import requests
import json

# 1.api 키 지정
apiKey = "4068d6f78e8aed97f6610b6f072ddb22"
# 2.날씨 확인할 도시 지정
cities = ["Seoul, KR", "Incheon, KR", "Osaka, JP", "New York, US"]

# 3.켈빈 -> 섭씨 변환 함수 정의
k2c = lambda k: k - 273.15

api = "http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}"

# 4. 각 도시 정보 추출
for name in cities:
    # API의 URL 구성
    url = api.format(city=name, key=apiKey)
    # 4-2. API 요청보내 데이터 추출
    r = requests.get(url)
    # 4.2. 결과를 JSON 형식 변환 : JSON 파일 = json.loads(변환대상 파일)
    data=json.loads(r.text)
    # 4.3. 결과 출력
    print("")
    if data['sys']['country'] == 'KR':
        print(f"+ 국가 = 한국")
    elif data['sys']['country'] == 'US':
        print(f"+ 국가 = 미국")
    elif  data['sys']['country'] == 'JP':
        print(f"+ 국가 = 일본")
    print(f"+ 도시 = {data['name']}")
    print(f"| 위도 = {data['coord']['lon']}")
    print(f"| 경도 = {data['coord']['lat']}")
    print("| 날씨 =", data["weather"][0]["description"])
    print("| 현재 기온 =", round(k2c(data["main"]["temp"]), 1))
    print("| 체감 기온 =", round(k2c(data["main"]["feels_like"]), 1))
    print("| 최저 기온 =", round(k2c(data["main"]["temp_min"]), 1))
    print("| 최고 기온 =", round(k2c(data["main"]["temp_max"]), 1))
    print(f"| 기압 = {data['main']['pressure']}")
    print(f"| 습도 = {data['main']['humidity']}")
    # print("| 최저 기온 =", k2c(data["main"]["temp_min"]))
    # print("| 최고 기온 =", k2c(data["main"]["temp_max"]))
    print(f"| 풍속 = {data['wind']['speed']}")
    print("")

print(r.text)




