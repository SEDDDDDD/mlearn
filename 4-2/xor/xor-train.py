from sklearn import svm

# XOR 계산 결과 데이터
xor_data = [
    #P, Q, result
    [0, 1, 1],
    [0, 0, 0],
    [1, 1, 0],
    [1, 0, 1]

]

# print(xor_data)


# 학습을 위해 데이터와 레이블 분리하기
data = []
label = []
for row in xor_data:
   p = row[0]
   q = row[1]
   r = row[2]
   data.append([p, q])      # 학습 데이터
   label.append(r)          # 레이블(정답)

# 데이터 학습하기

clf = svm.SVC()
# clf.fit(학습데이터, 정답)
clf.fit(data, label)         #### 모델링

# 데이터 예측하기
# 결과 = pre = clf.predict(테스트데이터)
pre = clf.predict(data)     #### 예측
print(f"예측결과 : {pre}")




# 결과 확인

ok = 0      # 정답을 맞힌 개수
total = 0   # 예측 수행 개수

for idx, answer in enumerate(label):
    p = pre[idx]
    if p == answer:
        ok += 1
    total += 1

print(f"정답률: {ok} / {total} = {ok/total}")



