import urllib.request as req
import gzip, os, os.path

# 저장 경로 지정 및 다운로드 사이트 URL

savepath = "./mnist"
baseurl = "http://yann.lecun.com/exdb/mnist/"
files = [
    "train-images-idx3-ubyte.gz",
    "train-labels-idx1-ubyte.gz",
    "t10k-images-idx3-ubyte.gz",
    "t10k-labels-idx1-ubyte.gz"
]

# 다운로드
if not os.path.exists(savepath):
    os.mkdir(savepath)

for file in files:
    url = baseurl + "/" + file      # http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz
    loc = savepath + "/" + file     # ./mnist/train-images-idx3-ubyte.gz
    print(f"downloadurl : {url}")
    print(f"path : {loc}")

    if not os.path.exists(loc):
        req.urlretrieve(url, loc)


# gzip 압축 해제
for file in files:
    # 다운로드 받은 파일
    gz_file = savepath + "/" + file
    # 가져온 데이터를 저장할 파일
    raw_file = savepath + "/" + file.replace(".gz", "")

    with gzip.open(gz_file, "rb") as fp:
        body = fp.read()
        with open(raw_file, "wb") as w:
            w.write(body)