import urllib.request as req
local = "whitewineinfo.csv"
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv"
req.urlretrieve(url, local)
print("ok")