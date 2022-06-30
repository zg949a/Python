import csv

filename = "./ClassInfo.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for index, column_header in enumerate(header_row):
        print(index+1, column_header)