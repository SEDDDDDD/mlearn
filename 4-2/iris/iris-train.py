from sklearn import svm, metrics
import random, re
import pandas as pd





        # 데이터 수집 (붓꽃)
csv = []
with open("iris.csv", "r", encoding='utf-8') as fp:
    # 한줄씪 읽어오기
    for line in fp:
        line = line.strip()             # 줄바꿈 제거
        cols = line.split(',')          # 쉼표를 구분자로 데이터 분할
        # print(cols)
        # print(type(cols[0]))
        csv.append(cols)

        # 데이터 정제
del csv[0]

# print(csv)

        # 데이터 섞기
random.shuffle(csv)

        # 학습 데이터, 테스트 데이터 분할(2:1)
total_len = len(csv)        # 150
train_len = int(total_len * 2 / 3)

# print(total_len)
# print(train_len)

train_data = []
train_label = []
test_data = []
test_label = []

for i in range(total_len):
    data = csv[i][0:4]
    label = csv[i][4]
    # print(f"data : {data}\t label : {label}")
    if i < train_len:
        train_data.append(data)
        train_label.append(label)
    else:
        test_data.append(data)
        test_label.append(label)

        # 모델링
clf = svm.SVC()
clf.fit(train_data, train_label)
        # 예측
pre = clf.predict(test_data)
        # 결과 : 테스트 데이터를 사용해 예측한 결과를 테스트 레이블과 비교
ac_score = metrics.accuracy_score(test_label, pre)
print(f"정답률 : {ac_score}")