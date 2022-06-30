import csv

filename = "./ClassInfo.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #从文件中获取数据
    classids = []
    for row in reader:
        classid = int(row[1000])
        classids.append(classid)

print(classids)