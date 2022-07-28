import openpyxl

# 목표 : (전체인구 - 서울인구) 데이터를 엑셀로 저장

# 1. 엑셀 파일 열기
filename = "stat_104102.xlsx"
book = openpyxl.load_workbook(filename)
# print(book)

# 2. 활성화 된 시트 추출
sheet = book.active

# 3. 서울 인구를 제외한 인구 구해서 쓰기

# 3-1. 엑셀 읽기
for i in range(0, 10):
    total = sheet[chr(66 + i) + "4"].value  # 연도별 전체 인구
    seoul = sheet[chr(66 + i) + "5"].value  # 연도별 서울 인구
    result = total - seoul

# 3-2. 엑셀 쓰기
    sheet[chr(66 + i) + "25"] = result
    cell = sheet[chr(66 + i) + "25"]

# 3-3. 폰트와 색상 변경
    cell.font = openpyxl.styles.Font(size=12, color="FF0000")
    cell.number_format = cell.number_format
sheet["A25"] = "서울제외인구"     # 시트 A25 셀에 서울제외인구 입력

# 4. 엑셀 저장

filename = "population.xlsx"
book.save(filename)
print("ok")