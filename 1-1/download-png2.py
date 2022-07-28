import urllib.request

# 파일로 저장

url = "https://mblogthumb-phinf.pstatic.net/20150613_233/aaaa3707_1434196005621iGF1M_JPEG/hq-widescreen-wallpapers-JnzO1.jpg?type=w2"

savename = "test1.png"

mem = urllib.request.urlopen(url).read()

with open(savename, mode="wb") as f:    # mode= "wb" 쓰기모드이지만 b 가 붙은 경우 binary(이진수) 쓰기모드
    f.write(mem)
    print("저장되었습니다!")

