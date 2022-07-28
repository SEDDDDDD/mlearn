from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd

# 키와 몸무게 데이터 csv 파일로부터 읽기
table = pd.read_csv("bmi.csv")
# print(table)
# print(type(tbl))
# 컬럼(열)을 자르고 정규화 하기
label = table["label"]
w = table["weight"] / 100 # 최대 100kg 가정
# print(w)
h = table["height"] / 200 # 최대 200cm 가정
# print(h)

# concat,
# axis(축) : 0 인경우 세로(상 하) 병합
#            1 인경우 가로(좌 우) 병합
# axis : 여러개의 동일형태 데이터 프레임 합치기

wh = pd.concat([w, h], axis= 1)
# print(wh)

# # 학습 데이터와 테스트 데이터 분할
# train_test_split 옵션값
# test_size : 테스트 데이터 비율 / default : 0.25
# shuffle : 데이터 섞을지 여부 설정 True, false / default : True


train_data, test_data, train_label, test_label = \
    train_test_split(wh, label, test_size=0.25)

# print(train_data)
# print(test_data)


# 학습
clf = svm.SVC()
# clf = svm.LinearSVC()
clf.fit(train_data, train_label)

# 예측
predict = clf.predict(test_data)

# 결과확인

ac_score = metrics.accuracy_score(test_label, predict)
print(f"정확도 : {ac_score}")
ac_report = metrics.classification_report(test_label, predict)
print(f"{ac_report}")

