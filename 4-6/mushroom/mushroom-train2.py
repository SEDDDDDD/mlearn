import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split

# 목표 : 버섯의 특징 기호를 리스트로 나타내고
# one hot encoding 방식으로 코드 변환


#데이터 읽기
mr = pd.read_csv("mushroom.csv", header=None)

# 데이터와 레이블 분할 / 데이터 내부 기호를 숫자로 변환
data = []
label = []
attr_list = []

cnt = 0
for row_index, row in mr.iterrows():
    #0~8123    #0~21, 문자데이터
    label.append(row.loc[0])        # 데이터프레임 인덱싱 하는법
                                    # ['p'] ,x,s,n,t,p,f,c,n,k,e,e,s,s,w,w,p,w,o,p,k,s,u

    exdata = []
    cnt += 1
    if cnt < 2:

        # 각각의 행으로 분할 =>
        for col_idx, val in enumerate(row.loc[1:]):
            # print(col_idx, end=' ')     # 속성 인덱스값(22개), 0~21
            # print(val, end=' ')         # 속성 값(22개), 문자데이터
            if row_index == 0:              # p,x,s,n,t,p,f,c,n,k,e,e,s,s,w,w,p,w,o,p,k,s,u
                attr = {"dic":{}, "cnt":0}  # {'dic':{}, 'cnt': 0}
                attr_list.append(attr)      # [{'dic':{}, 'cnt': 0}]
            else:
                attr = attr_list[col_idx]
            # print(attr_list)
            # attr_list[col_idx]

            # 버섯의 특징기호를 리스트로 표현
            d = [0,0,0,0,0,0,0,0,0,0,0,0]        # 최대 속성값 개수가 12개

            # 어디에 1을 찍어줄 것인가?
            if val in attr["dic"]:          # 만약 attr["dic"]에 val 값이 있으면,
                idx = attr["dic"][val]
            else:                           # 만약 attr["dic"]에 val 값이 없으면,
                idx = attr["cnt"]
                attr["dic"][val] = idx
                attr["cnt"] += 1
            d[idx] = 1      # 1이 찍힌 n 번째의 문자를 의미
            # [ [1,0,0,0,0,0,0,0,0,0,0,0], * 22개 ]
            exdata += d
        data.append(exdata)
print(label[0])
# print(data)


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




