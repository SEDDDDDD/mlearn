import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn import svm
from sklearn.preprocessing import StandardScaler



csv = pd.read_csv('WineDataset.csv')
# print(csv.head())

data = csv.drop('Wine', axis=1).values # csv 에서 label 값을 제거한 데이터 값을 data에 할당

# print(data)

label = csv["Wine"].values   # 레이블 값만 label 에 리스트로 저장

# 데이터 / 레이블 분류
train_data, test_data, train_label, test_label = train_test_split(data, label, test_size=0.3)


sc_X = StandardScaler()
train_data = sc_X.fit_transform(train_data)
test_data = sc_X.transform(test_data)




# clf = GaussianNB()
clf = svm.SVC(kernel='linear')



clf.fit(train_data, train_label)        # 학습

predict = clf.predict(test_data)        # 예측

score = accuracy_score(test_label, predict)     # 결과

print(score)


# 시각화
# seaborn 이용
cmap = sns.cm._cmap_r # 그래프 컬러 설정
plt.rcParams["axes.unicode_minus"]=False  # 마이너스 부호 때문에 혹시라도 한글이 깨지는 경우를 방지하기 위해 주는 옵션
plt.rcParams['font.family'] = 'Malgun Gothic' # 폰트 설정

# 분류 시각화를 위해 confusion_matrix(오차 행렬) 사용
# sns.heatmap(confusion_matrix(test_label, predict), cmap=cmap, annot=True)
# cmap : 그래프 컬러 설정, annot : 그래프 각 cell에 값 표기
sns.heatmap(confusion_matrix(test_label, predict), cmap=cmap, annot=True)

plt.title('와인 품질 예측')

plt.xlabel('예측값')
plt.ylabel('실제값')

plt.show()

# 산점도 표현 알아봐라