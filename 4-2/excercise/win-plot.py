import matplotlib.pyplot as plt
import pandas as pd

csv = pd.read_csv("redwineinfo.csv")
print(csv)

fig = plt.figure()
ax = fig.add_subplot(2, 3, 4)  # (1,1,1) => 1x1 그리드, 첫번째 서브플롯


# 데이터 프레임으로부터 특정 컬럼의 값 가져오기
# 데이터 프레임 인덱싱 방법
# b = csv.loc["4"]
# print(b)

# 서브 플롯 전용 - 지정한 레이블을 임의의 색으로 칠하기
def scatter(label, color):
    b = csv.loc[label]
    # 산포도 그리는 함수
    # 해당하는 서브플롯.scatter(x축위치, y축위치)
    ax.scatter(b["fixed acidity"], b["volatile acidity"], b["citric acid"],
               b["residual sugar"], b["chlorides"], b["free sulfur dioxide"],
               b["total sulfur dioxide"], b["density"], b["pH"], b["sulphates"],
               b["alcohol"],
               c=color,
               label=label)

scatter("4", "purple")
scatter("5", "red")
scatter("6", "blue")
scatter("7", "red")

ax.legend()  # 범례 표시
plt.savefig("redWine-test.png")