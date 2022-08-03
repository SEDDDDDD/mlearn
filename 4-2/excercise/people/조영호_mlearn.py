import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix



csv = pd.read_csv('WineDataset.csv')
# print(csv.head())

data = csv.drop('Wine', axis=1).values # csv 에서 label 값을 제거한 데이터 값을 data에 할당

# print(data)

label = csv["Wine"].values   # 레이블 값만 label 에 리스트로 저장


train_data, test_data, train_label, test_label = train_test_split(data, label, test_size=0.3)
# 데이터 / 레이블 분류
clf = GaussianNB()
# 나이브베이즈 분류기 GaussianNB 적용


clf.fit(train_data, train_label)        # 학습

predict = clf.predict(test_data)        # 예측

score = accuracy_score(test_label, predict)     # 결과

print(score)


# 시각화
# seaborn 이용
cmap = sns.cm._cmap_r # 그래프 컬러 설정
plt.rcParams["axes.unicode_minus"]=False  # 마이너스 부호 때문에 혹시라도 한글이 깨지는 경우를 방지하기 위해 주는 옵션
plt.rcParams['font.family'] = 'Malgun Gothic' # 폰트 설정

# 분류 시각화를 위해 confusion_matrix(혼돈 행렬) 사용
sns.heatmap(confusion_matrix(test_label, predict), cmap=cmap, annot=True)
# cmap : 그래프 컬러 설정, annot : 그래프 각 cell에 값 표기

plt.title('Confusion Matrix')

plt.xlabel('예측값')
plt.ylabel('실제값')

plt.show()