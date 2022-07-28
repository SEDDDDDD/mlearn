import pandas as pd
from sklearn import svm
from sklearn import metrics

xor_input = [
    #P, Q, result
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]

]


# loc함수 loc( 행, 열 )
xor_df = pd.DataFrame(xor_input)
xor_data = xor_df.loc[0:3,0:1] # 데이터
xor_label = xor_df.loc[0:3,2] #테이블

# 데이터 학습하기
clf = svm.SVC()                 # 알고리즘 선택
clf.fit(xor_data, xor_label)    # 학습(모델링) clf.fit(학습데이터, 정답(라벨))
pre = clf.predict(xor_data)     # 예측 -> 답
print(pre)

ac_score = metrics.accuracy_score(xor_label, pre)

print(ac_score)
