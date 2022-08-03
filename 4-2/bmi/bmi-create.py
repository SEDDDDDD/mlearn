# csv 파일에 무작위로 키와 몸무게를 생성해서 저장
import random


# bmi 를 계산해서 레이블을 리턴하는 함수
def calc_bmi(h, w):  # h : 키 , w : 몸무게
    bmi = w / (h / 100) ** 2
    if bmi < 18.5:
        return "thin"
    if bmi < 22.9:
        return "normal"
    return "fat"


# 출력파일 준비 bmi.csv
fp = open("bmi.csv", "w", encoding="utf-8")
fp.write("height,weight,label\r\n")

cnt = {"thin": 0, "normal": 0, "fat": 0}
# 무작위로 데이터 생성
for i in range(40000):
    h = random.randint(150, 200)
    w = random.randint(40, 120)
    # print(f"신장 : {h}\t 몸무게 : {w}\t 결과 : {label}\r\n")

    label = calc_bmi(h, w)
    cnt[label] += 1

    fp.write("{0}, {1}, {2}\r\n".format(h, w, label))
fp.close()

print("csv 생성완료", cnt)
