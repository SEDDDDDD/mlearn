import pandas as pd
from sklearn import svm
from sklearn import metrics
from sklearn.model_selection import train_test_split

train_filename = "./mnist/train.csv"
t10k_filename = "./mnist/t10k.csv"

# csv 파일 읽어 가공하기
def load_csv(fname):
    labels = []
    images = []

    # 학습데이터, 테스트데이터 csv => 리스트형태

    with open(fname, "r") as f:
        for line in f:
            cols = line.split(',')
            # print(cols)
            labels.append(cols.pop(0))
            vals = list(map(lambda n:int(n) / 256, cols))
            images.append(vals)
    # print(images)
    return {"labels" : labels, "images" : images}

train_data = load_csv("./mnist/train.csv")
print(train_data)
test_data = load_csv("./mnist/t10k.csv")
print(test_data)




# 알고리즘
clf = svm.SVC()

# 학습
clf.fit(train_data["images"], train_data["labels"])

# 예측
predict = clf.predict(test_data["images"])

# 정확도
ac_score = metrics.accuracy_score(test_data["labels"], predict)
print(f"정확도 : {ac_score}")


