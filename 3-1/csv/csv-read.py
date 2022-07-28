import codecs

filename = "list-euckr.csv"
csv = codecs.open(filename, "r", "euc_kr").read()
print(csv)

data = []

rows = csv.split("\r\n")

print(rows)
for row in rows:
    if row == "": continue
    cells = row.split(",")
    data.append(cells)

for c in data:
    print(c[1],c[2])