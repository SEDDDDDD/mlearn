# 연도별 인구 1위 구하기
import openpyxl

filename = "population.xlsx"
book = openpyxl.load_workbook(filename)

book.active(filename)



