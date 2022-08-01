from sklearn import svm, metrics
import pandas as pd
from sklearn import model_selection
import re

# csv 읽어오기
csv = pd.read_csv("iris.csv")

# 리스트를 훈련 / 테스트 데이터 분할
data = csv[["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"]]
label = csv["Name"]


# 교차 검증 하기
clf = svm.SVC()
scores = model_selection.cross_val_score(clf, data, label, cv=5)
print(f"각각의 정답률 : {scores}")
print(f"평균 정답률 : {scores.mean()}")



