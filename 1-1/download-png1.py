import urllib.request

url = "https://mblogthumb-phinf.pstatic.net/20150613_233/aaaa3707_1434196005621iGF1M_JPEG/hq-widescreen-wallpapers-JnzO1.jpg?type=w2"

savename = "test.png"

urllib.request.urlretrieve(url, savename)
print("저장 되었습니다!!")
