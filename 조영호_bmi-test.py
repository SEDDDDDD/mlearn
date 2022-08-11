from sklearn import metrics
from sklearn.model_selection import train_test_split,c
import pandas as pd
from sklearn import svm

tbl = pd.read_csv("bmi.csv")

label = tbl["label"]
w = tbl["weight"]/ 100
h = tbl["height"]/ 200
wh = pd.concat([w, h], axis=1)

data_train, data_test, label_train, label_test = train_test_split(wh, label, test_size=0.25)

clf = svm.SVC()
clf.fit(data_train, label_train)
pre = clf.predict(label_test)


ac_score = metrics.accuracy_score(label_test, pre)
print(f"정확도: {ac_score}")