# This tutorial deals with reading CSV (Comma Separated Values) files

import csv

filename = "student_grades.csv"
rows = []
fields = []


with open(filename, mode="r", encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    fields = next(csvreader)

    for row in csvreader:
        rows.append(row)

    # get total number f rows
    print(f"Total no of rows: {csvreader.line_num}")

# print field names
print("Field names: ", ",".join(fields))

# print rows
for row in rows:
    for col in row:
        print(col, end="\t")
    print("\n")


