import urllib.request

url = "https://n.news.naver.com/article/421/0006200438?cds=news_media_pc&type=editn"
res = urllib.request.urlopen(url)

data = res.read()

text = data.decode("utf-8")

print(text)