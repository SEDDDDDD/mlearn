from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.callbacks import EarlyStopping
import pandas as pd
import numpy as np

csv = pd.read_csv('../5-4/bmi.csv')

# 데이터 정규화
csv["weight"] /= 100
csv["height"] /= 100

X = csv[["weight", "height"]]

# 레이블
bclass = {" thin":[1, 0, 0]," normal":[0, 1, 0], " fat":[0, 0, 1]}

# numpy.empty(행, 렬) 행, 렬 로 인자가 비어있는 배열 생성
y = np.empty((20000, 3))
for idx, val in enumerate(csv["label"]):
    y[idx] = bclass[val]

X_train, y_train = X[1:15001], y[1:15001]
X_test, y_test = X[15001:20001], y[15001:20001]


# 모델 구축
model = Sequential()

# 모델 구조 정의
# add() 함수 : 레이어 스택 위에 레이어 인스턴스를 추가
#  - layer : 레이어 인스턴스
# Dense : 여러 레이어로부터 계산된 정보를 하나로 모은 자료
# Activation : 출력에 활성화 함수를 적용하는 계층
#  - relu : 입력값이 0보다 작으면 0으로 출력, 0보다 크면 입력값그대로 출력하는 유닛
# Dropout 입력에 dropout을 적용
#  - Dropout 계층은 훈련시간동안 각단계에서 특정빈도로 입력단위를 무작위로 0으로 설정하여 과적합을 방지

model.add(Dense(512, input_shape=(2,)))
model.add(Activation('relu'))
model.add(Dropout(0.1))
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.1))
model.add(Dense(3))
model.add(Activation('softmax'))





# 학습 과정 구성 필수
# loss(손실) : 모델과 특성간 차이
# optimizer(최적화) : 손실을 줄이는 과정
# metrics : 훈련 및 테스트 중에 모델이 평가할 목록
#  - 일반적으로 merics = ['accuracy']사용

model.compile(optimizer="rmsprop",
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# 데이터 학습


model.fit(
    X_train, y_train,
    batch_size=100,
    epochs=20,
    validation_split=0.1,
    # EarlyStopping : 손실값이 개선되지 않으면 학습을 종료
    # patience 만큼 epochs를 기다림
    # monitor 학습 조기 종료를 위해 관찰하는 항목
    callbacks=[EarlyStopping(monitor='val_loss', patience=2)],
    # 함수 수행시 발생하는 정보를 상세하게 출력할 것인지 여부 선택(0:출력안함, 1:자세히 출력, 2: 함축적 출력)
    verbose=1
)

# 테스트 데이터로 평가

score = model.evaluate(X_test, y_test)
print("score = ", score[0])
print("accuracy = ", score[1])