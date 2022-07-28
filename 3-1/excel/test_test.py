import openpyxl

filename = "population.xlsx"
book = openpyxl.load_workbook(filename)

# 22행, 23행의 출처 및 주석 삭제
sheet = book.active

for i in range(0,2):
    sheet[chr(65 + i) + "22"] = ""
    sheet[chr(65 + i) + "23"] = ""

filename = "population_del.xlsx"
book.save(filename)

# 인구수로 따졌을때 제 2의 대도시는 어디인가


data=[]
for row in sheet.rows:
    data.append([
        row[0].value,
        row[10].value
    ])
# print(data)

del data[0:4]
del data[17:21]

# print(data)

data = sorted(data, key=lambda x:x[1], reverse=True)

print(data[2])


# 제2의 대도시와 서울의 인구 차이 B24 셀에 입력

seoul = int(data[1][1])
busan = int(data[2][1])

result = seoul - busan

print(result)
sheet["B24"] = f"제2의 대도시와 서울의 인구차이 : {result}"


book.save(filename)
print('a')