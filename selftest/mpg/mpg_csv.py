import urllib.request as req
local = "mpg.csv"
url = "http://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data"
req.urlretrieve(url, local)
print("ok")