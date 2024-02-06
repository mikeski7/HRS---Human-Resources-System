import csv

with open('emp_data.csv', 'r') as infile:
    reader = csv.reader(infile)
    lines = 0
    for row in reader:
        lines += 1

print(lines)