import matplotlib.pyplot as plt
import pandas as pd

table = pd.read_csv("wineinfo.csv")

print(table)

# 그래프 그리기
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)  # (1,1,1) => 1x1 그리드, 첫번째 서브플롯


# 데이터 프레임으로부터 특정 컬럼의 값 가져오기
# 데이터 프레임 인덱싱 방법
# df.loc["row", "column"]
# t = table.loc["thin"]
# print(t)
# n = table.loc["normal"]
# o = table.loc["overweight"]
# f = table.loc["fat"]


# 서브 플롯 전용 - 지정한 레이블을 임의의 색으로 칠하기
def scatter(label, color):
    data = table.loc[label]
    # 산포도 그리는 함수
    # 해당하는 서브플롯.scatter(x축위치, y축위치)
    ax.scatter(data["weight"], data["height"], c=color, label=label)

scatter("thin", "purple")
scatter("normal", "red")
scatter("overweight", "blue")
scatter("fat", "red")


ax.legend()  # 범례 표시
plt.savefig("bmi-test.png")
