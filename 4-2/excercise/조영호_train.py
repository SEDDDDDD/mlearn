import pandas as pd
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

# 데이터 수집
csv = pd.read_csv("redwineinfo.csv", sep=';')  # csv 파일의 구분자가 ';' 이기 때문에 속성에 구분자 표시




data = csv.iloc[:, :-1]  # quality 값을 제외한 전체 행,열 의 값을 추출
label = csv.iloc[:, -1]  # quality 값만 추출
print(data)
data = data.values          # 각 행의 값을 data 리스트에 담는다
label = label.values        # label 값(quality) 을 label 리스트에 담는다
print(data)
# 학습 / 테스트 데이터 , 레이블 분할

train_data, test_data, train_label, test_label = \
    train_test_split(data, label, random_state=3)


# 모델링
# clf = ExtraTreesClassifier()
# clf = svm.LinearSVC()
# clf = svm.SVC()
# clf = svm.SVR()

clf = DecisionTreeClassifier()

clf.fit(train_data, train_label)

# 예측
pre = clf.predict(test_data)

# 결과 : 테스트 데이터를 사용해 예측한 결과를 테스트 레이블과 비교
ac_score = metrics.accuracy_score(test_label, pre)
print(f"정답률 : {ac_score}")


