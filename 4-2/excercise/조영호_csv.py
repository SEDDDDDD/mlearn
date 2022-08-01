import urllib.request as req
local = "redwineinfo.csv"
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
req.urlretrieve(url, local)
print("ok")