import csv, codecs

# csv 파일 열기
filename = "list-euckr.csv"
fp = codecs.open(filename, "r", "euc_kr")



# csv한줄씩 읽기

reader = csv.reader(fp, delimiter =",", quotechar='"')
print(reader)

for cells in reader:
    print(cells[1], cells[2])










