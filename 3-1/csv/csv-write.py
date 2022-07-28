import csv, codecs

with codecs.open("test.csv", "w", "euc_kr") as fp:
    writer = csv.writer(fp, delimiter=",", quotechar='"')
    writer.writerow(["id", "이름", "가격"])
    writer.writerow(["1001", "이름", "30000"])
    writer.writerow(["1002", "sd카드", "50000"])
    writer.writerow(["1003", "마우스", "170000"])
