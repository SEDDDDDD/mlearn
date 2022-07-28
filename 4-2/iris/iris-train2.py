import pandas as pd
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split

# 데이터 수집 (붓꽃)
csv = pd.read_csv("iris.csv")

# 필요한 열 출
# csv[컬럼명]
csv_data = csv[["SepalLength","SepalWidth","PetalLength","PetalWidth"]]
csv_label = csv["Name"]
# print(csv_label)

# 학습데이터(3/4)와 테스트 데이터(1/4) 분할
# 학습데이터, 테스트데이터, 학습레이블, 테스트레이블 = train_test_split(학습데이터, 학습레이블)
train_data, test_data, train_label, test_label = \
    train_test_split(csv_data, csv_label)
# print(train_data)


# # 모델링
clf = svm.SVC()                     # 분석기
clf.fit(train_data, train_label)
#
# # 예측
pre = clf.predict(test_data)
#
#
# # 결과 : 테스트 데이터를 사용해 예측한 결과를 테스트 레이블과 비교
ac_score = metrics.accuracy_score(test_label, pre)
print(f"정답률 : {ac_score}")