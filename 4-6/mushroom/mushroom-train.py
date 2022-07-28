import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split


#데이터 읽기
mr = pd.read_csv("mushroom.csv", header=None)

# 데이터와 레이블 분할 / 데이터 내부 기호를 숫자로 변환
data = []
label = []

# iterrows() : 데이터 전처리 진행시,
# 데이터 프레임에서 행에 반복적으로 접근하면서 값을 추출하거나 조작할 때
# 데이터에 접근하는 방법
for row_index, row in mr.iterrows():
    label.append(row.loc[0])        # 데이터프레임 인덱싱 하는법
    row_data = []
    for attr in row.loc[1:]:
        # print(attr)
        row_data.append(ord(attr))
    data.append(row_data)


# 학습데이터 / 테스트데이터 분할
train_data, test_data, train_label, test_label = \
    train_test_split(data, label)


# 모델학습
clf = RandomForestClassifier()
clf.fit(train_data, train_label)

# 예측
predict = clf.predict(test_data)

#정답률 확인
ac_score = metrics.accuracy_score(test_label, predict)
cl_report = metrics.classification_report(test_label, predict)
print(f"정답률 : {ac_score}")
print(f"리포트 : {cl_report}")