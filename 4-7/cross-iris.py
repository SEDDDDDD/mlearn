from sklearn import svm, metrics
import random, re

# 붓꽃 csv 파일 읽기
lines = open("iris_test.csv", "r", encoding="utf-8").read().split("\n")

# 숫자(float)으로 변환 함수
f_tonum = lambda n: float(n) if re.match(r'^[0-9\.]+$', n) else n
# 컬럼 값을 추출하는 함수
f_cols = lambda li: list(map(f_tonum, li.strip().split(',')))
csv = list(map(f_cols, lines))
# print(csv)

del csv[0]      # 헤더 제거
random.shuffle(csv)     # 데이터 섞기

# 데이터를 k 개로 분할
k = 5

csvk = [ [] for i in range(k) ]
# print(csvk)

for i in range(len(csv)):
    # print(i % k)
    csvk[i % k].append(csv[i])

# print(csvk)



# 데이터 리스트를 훈련 데이터 / 테스트 데이터로 분할
# 행 개수,
data = []
label = []

for testc in csvk:
    # print(testc)
    trainc = []
    for i in csvk:
        if i != testc:
            trainc += i
print(trainc)





# # 학습
# clf = svm.SVC()
# clf.fit(train_data, train_label
#
# #예측
# predict = clf.predict(test_data)
#
#
#
# # 정답률 확인
#
# metrics.accuracy_score(test_label, predict)
