import pandas as pd
import seaborn as sns
import numpy as np
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from matplotlib import pyplot as plt

# 데이터 수집
csv = pd.read_csv("redwineinfo.csv", sep=';')  # csv 파일의 구분자가 ';' 이기 때문에 속성에 구분자 표시




data = csv.iloc[:, :-1]  # quality 값을 제외한 전체 행,열 의 값을 추출
label = csv.iloc[:, -1]  # quality 값만 추출

# data = data.values          # 각 행의 값을 data 리스트에 담는다
# label = label.values        # label 값(quality) 을 label 리스트에 담는다

# 학습 / 테스트 데이터 , 레이블 분할

train_data, test_data, train_label, test_label = \
    train_test_split(data, label, random_state=3)


# 모델링
clf = RandomForestClassifier()
clf2 = svm.SVC()

clf.fit(train_data, train_label)
clf2.fit(train_data, train_label)

# 예측
pre = clf.predict(test_data)
pre2 = clf2.predict(test_data)

# 결과 : 테스트 데이터를 사용해 예측한 결과를 테스트 레이블과 비교
ac_score = metrics.accuracy_score(test_label, pre)
ac_score2 = metrics.accuracy_score(test_label, pre2)
print(f"SVC 정답률 : {ac_score2}")
print(f"랜덤포레스트 정답률 : {ac_score}")


cmap = sns.cm._cmap_r # 그래프 컬러 설정

sns.heatmap(confusion_matrix(test_label, pre2), cmap=cmap, annot=True)
svc_score = accuracy_score(test_label, pre2)
rf_confusion_matrix = confusion_matrix(test_label, pre)
rf_score = accuracy_score(test_label, pre)
print("랜덤 포레스트 시각화\n", rf_confusion_matrix)
print(rf_score*100)

plt.title("SVC confusion_matrix")
plt.xlabel("실제값")
plt.ylabel("예측값")
plt.show()
print(svc_score*100)




