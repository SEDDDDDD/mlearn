import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm, metrics
import numpy as np
import random

df = pd.read_csv("voice.csv")


df.label = [1 if each == "male" else 0 for each in df.label]

# assignment to variable
y = df.label.values
x_data = df.drop(["label"], axis = 1)

## Normalization
x = (x_data - np.min(x_data)) / (np.max(x_data) - np.min(x_data)).values

# Train test split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2, random_state = 42)
x_train = x_train.T
x_test = x_test.T
y_train = y_train.T
y_test = y_train.T

clf = svm.SVC()                     # 분석기
clf.fit(x_train, y_train)
#
# # 예측
pre = clf.predict(x_test)
#
#
# # 결과 : 테스트 데이터를 사용해 예측한 결과를 테스트 레이블과 비교
ac_score = metrics.accuracy_score(y_test, pre)
print(f"정답률 : {ac_score}")




# csv_data=[["meanfreq","sd","median","Q25","Q75","IQR","skew","kurt","sp.ent",
#            "sfm","mode","centroid","meanfun","minfun","maxfun","meandom",
#            "mindom","maxdom","dfrange","modindx"]]
#
# csv_label = ["label"]
#
# train_data, test_data, train_label, test_label = \
#     train_test_split(csv_data, csv_label)
#
#
# clf = svm.SVC()                     # 분석기
# clf.fit(train_data, train_label)
#
# # # 예측
# pre = clf.predict(test_data)
#
# # # 결과 : 테스트 데이터를 사용해 예측한 결과를 테스트 레이블과 비교
# ac_score = metrics.accuracy_score(test_label, pre)
# print(f"정답률 : {ac_score}")