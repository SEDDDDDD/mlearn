import pandas as pd
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
from sklearn.ensemble import ExtraTreesClassifier

# 데이터 수집
csv = pd.read_csv("whitewineinfo.csv", sep=';')  # csv 파일의 구분자가 ';' 이기 때문에 속성에 구분자 표시

data = csv.iloc[:, :-1]  # quality 값을 제외한 전체 행,열 의 값을 추출
label = csv.iloc[:, -1]  # quality 값만 추출

data = data.values
label = label.values

# 학습 / 테스트 데이터 , 레이블 분할

train_data, test_data, train_label, test_label = \
    train_test_split(data, label)


# 모델링

clf = svm.SVC()


clf.fit(train_data, train_label)

# 예측
pre = clf.predict(test_data)

# 결과 : 테스트 데이터를 사용해 예측한 결과를 테스트 레이블과 비교
ac_score = metrics.accuracy_score(test_label, pre)
print(f"정답률 : {ac_score}")



