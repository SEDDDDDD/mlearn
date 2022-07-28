import pandas as pd

# 1. 엑셀파일 열기
filename = "stat_104102.xlsx"
sheet_name = "Sheet0"
book = pd.read_excel(filename, sheet_name=sheet_name, header = 2, engine='openpyxl') # header : 컬럼명 0행부터

# 2. 2018년도 인구로 정렬

book = book.sort_values(by=2021, ascending=False) #by 정렬 시 기준 , ascending false 내림차순 true 오름차순
print(book)