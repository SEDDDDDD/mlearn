from bs4 import BeautifulSoup
import urllib.request as req

url = "https://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=1156053500"

res = req.urlopen(url)

soup = BeautifulSoup(res,'html.parser')

title = soup.find("reh").string
wf = soup.find("wf").string
print(title)
print(wf)

