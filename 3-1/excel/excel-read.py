import openpyxl
# 목표 : 어느지역의 인구가 더많은가?

# 엑셀파일 열기
filename = "stat_104102.xlsx"
book = openpyxl.load_workbook(filename)
# print(book)

# 첫번째 시트 추출
sheet = book.worksheets[0]
# sheet2 = book.worksheets[1]
# print(type(sheet))

# 시트의 각행을 순서대로 추출

data = []
for row in sheet.rows:
    # print(row[0].value, end='\t')
    # print(row[1].value, end='\t')
    # print(row[2].value, end='\t')
    # print(row[3].value, end='\t')
    # print(row[4].value)
    data.append(
        [row[0].value,      # 지역명
         # row[1].value,      # 2012
         # row[2].value,      # 2013
         # row[3].value,      # 2014
         # row[4].value,      # 2015
         row[10].value      # 2016
         ]
    )
# print(data)


# 필요없는 줄 제거
del data[0]
del data[0]
del data[0]
del data[0]
del data[17]
del data[17]


# print(data)

# 데이터를 인구 순서로 정렬
data = sorted(data, key=lambda x:x[1])
# print(data)


# 순서대로 출력 ( 하위 5개 )
# enumerate(리스트)    : 각 데이터에 인덱스 번호를 매핑
#  -반환값 : 튜플( 인덱스 번호, 데이터값)
#  ex) (0, ['세종', 371])
for idx, content in enumerate(data):
    if idx >= 5:
        break
    print(idx+1, content[0], content[1])
